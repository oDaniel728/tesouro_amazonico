import curses
import os
from instancias import armazenamento, fcontainer, estado, cor4, timeline
from enums import teclas
from utils.termux import mudar_titulo_do_terminal
from utils.lapis import BAIXO, escrever_texto
from random import randint

armazenamento.carregar()
# estados
# region ESTADOS GERAIS

[get_frame, set_frame] = estado.criar(0)

[get_lastkey, set_lastkey] = estado.criar(0)

def __curkey_changed(old, new):
    if new != -1:
        set_lastkey(new)
[get_curkey, set_curkey] = estado.criar(0, __curkey_changed) # util para pegar teclas

[get_running, set_running] = estado.criar(True)

[get_debug, set_debug] = estado.criar(False)
# set_debug(True) # Mude para False para jogar normalmente

[get_event, set_event] = estado.criar('')

def __scene_changed(old, new):
    set_event('change_scene')
    set_frame(-1)
[get_scene, set_scene] = estado.criar(0, __scene_changed)

# endregion

# region ESTADOS USADOS PELO JOGO

[get_difficulty, set_difficulty] = estado.criar(0)
DIFF_NONE = 0
DIFF_FACIL = 1
DIFF_NORMAL = 2
DIFF_DIFICIL = 3

[get_language, set_language] = estado.criar(
    armazenamento.pegar("lang", 0)
)
LANG_PORTUGUES = 0
LANG_INGLES = 1
# traduzir(pt, eng) -> str
# - se a linguagem estiver em portugues, retorna pt
# - se a linguagem estiver em ingles, retorna eng
def trd(pt: str, eng: str) -> str:
    lang = get_language()
    if lang == LANG_PORTUGUES:
        return pt
    elif lang == LANG_INGLES:
        return eng
    return ''

armazenamento.add_estado("lang", get_language)

[get_tutorial_passed, set_tutorial_passed] = estado.criar(
    armazenamento.pegar("tutorial_passed", False)
)
armazenamento.add_estado("tutorial_passed", get_tutorial_passed)

[get_x, set_x] = estado.criar(0)
[get_y, set_y] = estado.criar(0)
[get_max_pos, set_max_pos] = estado.criar([5, 5])
pistas = list[str]() # Esta variável parece não estar sendo usada, 'dicas' é usada em seu lugar

posicoes = []
def _add_pos(x: int, y: int):
    posicoes.append([x, y])

def __dimentions_changed(old, new):
    curses.resize_term(*new)
    set_event("resize")
[get_dimensions, set_dimensions] = estado.criar([0, 0], __dimentions_changed)

[get_caixas, set_caixas] = estado.criar([])

[get_tesouro_pos, set_tesouro_pos] = estado.criar([0, 0])
[get_durability, set_durability] = estado.criar(0)

dicas = [''] # Esta é a lista global correta que está sendo usada

areas_achadas = []
# [[x1, y1], [x2, y2]]
def add_areas_achadas(x1: int, y1: int, x2: int, y2: int):
    areas_achadas.append([[x1, y1], [x2, y2]])

def dentro_de_areas_achadas(x: int, y: int) -> bool:
    for [x1, y1], [x2, y2] in areas_achadas:
        inicio_x = min(x1, x2)
        fim_x = max(x1, x2)

        inicio_y = min(y1, y2)
        fim_y = max(y1, y2)

        if (inicio_x <= x <= fim_x) and (inicio_y <= y <= fim_y):
            return True
    return False

[get_mode, set_mode] = estado.criar(0)
MODO_X = 0
MODO_Y = 1

def __notif_changed(old, new):
    set_event('change_notif')
[get_notif, set_notif] = estado.criar('')
# endregion

def gerar_caixas(scr: curses.window, colunas: int, linhas: int):
        mx, my = scr.getmaxyx()
        mx //= 2
        my //= 8

        caixas = []
        # grade
        for i in range(-linhas // 2, linhas // 2):
            for j in range(-colunas // 2, colunas // 2):
                cx, cy = (mx * 2) + (j * 2) + 1, my + (i * 2) + 2

                col = j + colunas // 2
                lin = i + linhas // 2

                if colunas % 2 != 0: col += 1
                if linhas % 2 != 0: lin += 1
                caixas.append([[cx, cy], [col, lin]])

        return caixas

# ganhou fácil (?)
[get_gfacil, set_gfacil] = estado.criar(armazenamento.pegar('gfacil', False))
# ganhou médio (?)
[get_gmedio, set_gmedio] = estado.criar(armazenamento.pegar('gmedio', False))
# ganhou difícil (?)
[get_gdificil, set_gdificil] = estado.criar(armazenamento.pegar('gdificil', False))

armazenamento.add_estado('gfacil', get_gfacil)
armazenamento.add_estado('gmedio', get_gmedio)
armazenamento.add_estado('gdificil', get_gdificil)

# region curses setup
curses.initscr()
curses.start_color()
# endregion

# region containeres
on_loop  = fcontainer.criar()
on_start = fcontainer.criar()
on_char  = fcontainer.criar()
# endregion

# region main loop
@on_loop.append
def loop(scr: curses.window, delta: float):
    # Cores

    COR_VERDE_LIMAO = cor4.rgba(60, 255, 0, 1)
    COR_CINZA = cor4.rgba(100, 100, 100, 1)
    COR_CINZA_CLARO  = cor4.rgba(200, 200, 200, 1)
    COR_BRANCO = cor4.rgb(255, 255, 255)

    COR_AZUL = cor4.rgba(0, 157, 255, 1)
    COR_VERMELHO = cor4.rgba(255, 71, 71, 1)
    COR_DOURADO = cor4.rgba(255, 187, 0, 1)

    # Pares
    
    PAR_VERDE_FUNDO_PRETO   = cor4.criar_par(COR_VERDE_LIMAO)
    PAR_VERDE_FUNDO_PRETO_I = PAR_VERDE_FUNDO_PRETO | curses.A_REVERSE

    PAR_AZUL_FUNDO_PRETO    = cor4.criar_par(COR_AZUL)
    PAR_AZUL_FUNDO_PRETO_I  = PAR_AZUL_FUNDO_PRETO | curses.A_REVERSE

    PAR_VERMELHO_FUNDO_PRETO= cor4.criar_par(COR_VERMELHO)
    
    PAR_DOURADO_FUNDO_PRETO = cor4.criar_par(COR_DOURADO)

    PAR_SEC    = cor4.criar_par(COR_CINZA, curses.COLOR_BLACK)
    PAR_NORMAL = cor4.criar_par(COR_CINZA_CLARO, curses.COLOR_BLACK)
    PAR_BRANCO = cor4.criar_par(COR_BRANCO, curses.COLOR_BLACK)

    # cores para o jogo
    COR_CAIXA_2 = cor4.rgba(229, 204, 153, 1)
    COR_CAIXA_1 = cor4.rgba(227, 127, 27, 1)
    COR_CAIXA_0 = cor4.rgba(134, 70, 21, 1)

    # Pares para o jogo
    PAR_CAIXA_2 = cor4.criar_par(COR_CAIXA_2, COR_BRANCO)
    PAR_CAIXA_1 = cor4.criar_par(COR_CAIXA_1, COR_BRANCO)
    PAR_CAIXA_0 = cor4.criar_par(COR_CAIXA_0, COR_BRANCO)

    PAR_SETA_X = cor4.criar_par(COR_VERDE_LIMAO)
    PAR_SETA_Y = cor4.criar_par(COR_VERMELHO)

    # region debugging

    if get_debug():
        scr.addstr(0, 0, f"{trd('cena','scene')}: {get_scene()}, {trd('evento','event')}: {get_event()}", PAR_SEC)
        scr.addstr(1, 0, f"{trd('frame','frame')}: {get_frame()}, key: {get_curkey()}", PAR_SEC)
        scr.addstr(2, 0, f"last_key: {get_lastkey()}", PAR_SEC)
        # scr.addstr(2, 0, f"{get_language() =}", PAR_SEC)
        # scr.addstr(3, 0, f"{get_difficulty() =}", PAR_SEC)

    # endregion

    #! cena tutorial
    def TUTORIAL(f: int):
        if f == 0:
            mudar_titulo_do_terminal(trd("Tesouro Amazônico - Bem-vindo", "Amazonic Treasure Hunt - Welcome"))
            scr.erase()

        elif f == 1:
            escrever_texto(scr, trd("TESOURO  AMAZÔNICO", "AMAZONIC TREASURE HUNT"), -1, 2, PAR_VERDE_FUNDO_PRETO, 0)

        elif f == 20:
            escrever_texto(scr,
                trd("Olá, seja bem vindo ao jogo!",
                    "Hello, welcome to the game!"),
                -1, 4, PAR_NORMAL, 0)

        elif f == 40:
            escrever_texto(scr,
                trd("Desenvolvido por um monte de gente :D",
                    "Developed by a lot of people :D"),
                -1, 5, PAR_NORMAL, 0)
            escrever_texto(scr,
                trd("(Use o scroll do mouse para dar zoom)",
                    "(Use the mouse scroll to zoom the terminal)"),
                -1, 6, PAR_NORMAL, 0, offset_x=-1)

        elif f == 60:
            escrever_texto(scr,
                trd("[1]: OK", "[1]: OK"),
                -1, 7, PAR_NORMAL, 0)

        elif f == 80:
            escrever_texto(scr,
                trd("Aperte [1] para concluir a ação `OK`",
                    "Press [1] to confirm the `OK` action"),
                -1, -1, PAR_SEC, 0, -1)

        if get_curkey() == 49:
            set_scene(1)

    #! cena menu
    def MENU_INICIAL(f: int):
        key = get_curkey()
        padding_x: int = 15

        if f == 0: 
            set_dimensions([12, 48])
            mudar_titulo_do_terminal(trd("Tesouro Amazônico", "Amazonic Treasure Hunt"))
            scr.erase()
            escrever_texto(scr, trd("TESOURO  AMAZÔNICO", "AMAZONIC TREASURE HUNT"), -1, 2, PAR_VERDE_FUNDO_PRETO, 0)

        if f == 1: 
            escrever_texto(scr, trd("Jogar", "Play"), -1, 4, PAR_NORMAL, 1, padx=padding_x, offset_x=1)
            escrever_texto(scr, "[1]:", -1, 4, PAR_NORMAL, -1, padx=padding_x, offset_x=1)
        
        if f == 2: 
            escrever_texto(scr, trd("Opções", "Options"), -1, 5, PAR_NORMAL, 1, padx=padding_x, offset_x=1)
            escrever_texto(scr, "[2]:", -1, 5, PAR_NORMAL, -1, padx=padding_x, offset_x=1)
        
        if f == 3: 
            escrever_texto(scr, trd("Sair", "Exit"), -1, 7, PAR_VERMELHO_FUNDO_PRETO, 1, padx=padding_x, offset_x=1)
            escrever_texto(scr, "[3]:", -1, 7, PAR_VERMELHO_FUNDO_PRETO, -1, padx=padding_x, offset_x=1)
        
        if key == (teclas.DIGIT1): # JOGAR
            set_scene(2)

        if key == (teclas.DIGIT2): # OPÇÕES
            set_scene(3)

        if key == (teclas.DIGIT3): # SAIR
            set_scene(4)

    #! cena jogar
    def JOGAR(f: int):
        padding_x: int = 15
        key = get_curkey()

        if f == 0: 
            mudar_titulo_do_terminal(trd("NÍVEL DE DIFICULDADE", "DIFFICULTY LEVEL"))
            scr.erase()
            escrever_texto(scr, trd("NÍVEL DE DIFICULDADE", "DIFFICULTY LEVEL"), -1, 2, PAR_AZUL_FUNDO_PRETO, 0)

        if f == 1: 
            escrever_texto(scr, trd("Fácil", "Easy"), -1, 4, PAR_NORMAL, 1, padx=padding_x, offset_x=1)
            escrever_texto(scr, "[1]:", -1, 4, PAR_NORMAL, -1, padx=padding_x, offset_x=1)
        
        if f == 2: 
            par = PAR_NORMAL
            if not get_gfacil(): par = PAR_SEC
            escrever_texto(scr, trd("Médio", "Normal"), -1, 5, par, 1, padx=padding_x, offset_x=1)
            escrever_texto(scr, "[2]:", -1, 5, par, -1, padx=padding_x, offset_x=1)
        
        if f == 3: 
            par = PAR_NORMAL
            if not get_gmedio(): par = PAR_SEC
            escrever_texto(scr, trd("Difícil", "Hard"), -1, 6, par, 1, padx=padding_x, offset_x=1)
            escrever_texto(scr, "[3]:", -1, 6, par, -1, padx=padding_x, offset_x=1)

        if f == 4: 
            escrever_texto(scr, trd("Voltar", "Back"), -1, 8, PAR_VERMELHO_FUNDO_PRETO, 1, padx=padding_x, offset_x=1)
            escrever_texto(scr, "[4]:", -1, 8, PAR_VERMELHO_FUNDO_PRETO, -1, padx=padding_x, offset_x=1)

        # teclas   
        if key == (teclas.DIGIT4): # VOLTAR
            set_scene(1)

        elif key == (teclas.DIGIT1): # FACIL
            set_difficulty(DIFF_FACIL)
            set_scene(5)

        elif key == (teclas.DIGIT2) and get_gfacil(): # MEDIO
            set_difficulty(DIFF_NORMAL)
            set_scene(5)

        elif key == (teclas.DIGIT3) and get_gmedio(): # DIFICIL
            set_difficulty(DIFF_DIFICIL)
            set_scene(5)

    #! cena jogo

    def _proximidade(min: int, max: int, x: int) -> int:
        d_min = abs(min - x)
        d_max = abs(max - x)

        if d_min < d_max:
            return min
        else:
            return max
    
     
    def _criar_pista(x: int, y: int, tx: int, ty: int) -> str:
        modo = get_mode()
        
        if modo == MODO_X:
            if x > tx:
                return trd('mais ao oeste', 'further west')
            elif x < tx:
                return trd('mais ao leste', 'further east')
            else:
                return trd('coluna correta!', 'correct column!')
        
        elif modo == MODO_Y:
            if y > ty:
                return trd('mais ao norte', 'further north')
            elif y < ty:
                return trd('mais ao sul', 'further south')
            else:
                return trd('linha correta!', 'correct row!')
        
        return "" # Não deve acontecer se a lógica de "found" estiver correta

    def JOGO(f: int): 
        x, y = get_x(), get_y()

        def _add_area_achada(x: int, y: int):
            tx, ty = get_tesouro_pos()
            maxx, maxy = get_max_pos()
            modo = get_mode()

            # Pega o maior índice VÁLIDO da grade
            max_coord_x = maxx - 1
            max_coord_y = maxy - 1

            if modo == MODO_X:
                if x < tx:                 # Tesouro está à direita
                    # Invalida tudo à esquerda (incluindo a coluna atual)
                    add_areas_achadas(0, 0, x, max_coord_y)
                elif x > tx:               # Tesouro está à esquerda
                    # Invalida tudo à direita (incluindo a coluna atual)
                    add_areas_achadas(x, 0, max_coord_x, max_coord_y)

            elif modo == MODO_Y:
                if y < ty:                 # Tesouro está abaixo
                    # Invalida tudo acima (incluindo a linha atual)
                    add_areas_achadas(0, 0, max_coord_x, y)
                elif y > ty:               # Tesouro está acima
                    # Invalida tudo abaixo (incluindo a linha atual)
                    add_areas_achadas(0, y, max_coord_x, max_coord_y)

        if f == 0: # dificuldades
            if get_difficulty() == DIFF_FACIL:
                set_max_pos([5, 5])
                set_durability(7)
            elif get_difficulty() == DIFF_NORMAL:
                set_max_pos([7, 7])
                set_durability(6)
                set_dimensions([18, 72])
            elif get_difficulty() == DIFF_DIFICIL:
                set_max_pos([10, 10])
                set_durability(5)
                set_dimensions([24, 96])

            #! gerar tesouro
            maxx, maxy = get_max_pos()
            set_tesouro_pos([randint(0, maxx - 1), randint(0, maxy - 1)])
            
            # Gera as caixas apenas uma vez
            set_caixas(gerar_caixas(scr, *get_max_pos()))

             
            set_x(0)
            set_y(0)
            set_mode(MODO_X)
            dicas.clear() # Limpa a lista de dicas
            dicas.append('') # Adiciona a dica inicial vazia
            areas_achadas.clear() # Limpa as áreas achadas

            return

        # Limpamos a tela no início de cada frame
        scr.erase()
        
        # Pega a lista de caixas gerada
        caixas = get_caixas()

        # === NOVA LÓGICA DE DESENHO ===
        for caixa in caixas:
            (cx, cy), [col, lin] = caixa
            
            attr = PAR_CAIXA_1 # Cor padrão
            
            if col == x and lin == y:
                attr = PAR_CAIXA_2 # Caixa selecionada
             
            elif (get_debug() and ([col, lin] == get_tesouro_pos())):
                attr = PAR_AZUL_FUNDO_PRETO # Mostra tesouro (debug)
            elif dentro_de_areas_achadas(col, lin):
                attr = PAR_CAIXA_0 # Área descoberta/errada
                
            scr.addstr(cy, cx * 2, "  ", attr | curses.A_REVERSE)

        # durabilidade
        durabilidade = get_durability()
        dur_cor = PAR_DOURADO_FUNDO_PRETO
        if durabilidade <= 2: # Alerta de pouca durabilidade
            dur_cor = PAR_VERMELHO_FUNDO_PRETO
        escrever_texto(scr, trd(f"{durabilidade} Usos restantes", f"{durabilidade} Uses remaining"), -1, 0, dur_cor, -1, offset_x=1, padx=2)

        # rosa dos ventos
        escrever_texto(scr, trd("norte", "north") + "     ", -1, 0, PAR_NORMAL, 1)
        escrever_texto(scr, trd("oeste -+- leste", "west -+- east "), -1, 1, PAR_NORMAL, 1)
        escrever_texto(scr, trd("      sul      ", "    south     "), -1, 2, PAR_NORMAL, 1)
        
        # dica mais recente
        if len(dicas) > 0:
            dica_mais_recente = dicas[-1]
            escrever_texto(scr, dica_mais_recente, -1, -1, PAR_NORMAL, -1, -1, offset_y=1)

        # dicas
        for i, dica in enumerate(['...'] + dicas[-4:]):
            escrever_texto(scr, dica, -1, -1, PAR_NORMAL, 1, -1, offset_y=-i + 1)

        # seta de modo
        (start_cx, start_cy), _ = caixas[0]
        x_grade = start_cx * 2
        y_grade = start_cy
        (end_cx, end_cy), _ = caixas[-1]
        largura_grade = (end_cx * 2 + 2) - x_grade
        altura_grade = (end_cy + 1) - y_grade

        minx, miny = x_grade, y_grade
        maxx, maxy = largura_grade, altura_grade

        if get_mode() == MODO_X:
            COR = PAR_SETA_X
        else:
            COR = PAR_SETA_Y

        scr.addstr(miny - 1, minx - 1, '+', COR)
        if get_mode() == MODO_X:
            for x_pos in range(minx, minx + maxx):
                scr.addstr(miny - 1, x_pos, '-', COR)
            scr.addstr(miny -  1, minx + maxx - 1, '>', COR)
        elif get_mode() == MODO_Y:
            for y_pos in range(miny, miny + maxy):
                scr.addstr(y_pos, minx - 1, '|', COR)
            scr.addstr(maxy + miny - 1, minx - 1, 'V', COR)


        #! eventos
        if get_event('mine_box'):
            if [x, y] == get_tesouro_pos():
                set_event("found") # ACHOU!
            else:
                # Só minera e gasta durabilidade se não for uma área já achada
                if not dentro_de_areas_achadas(x, y):
                    dica = _criar_pista(x, y, *get_tesouro_pos())
                    dicas.append(dica)
                    set_event("mined") # <--- Evento que gasta durabilidade
                    _add_area_achada(x, y)
                else:
                    # Área já minerada, não faz nada e não gasta
                    pass

        if not get_tutorial_passed():
            if f < 60:
                escrever_texto(
                    scr, trd("Mova usando [WASD] e setas", "Move using [WASD] and arrows"), -1, -1, PAR_NORMAL, 0, 0, offset_y=1
                )
            elif f < 120:
                escrever_texto(
                    scr, trd("Aperte [E] para cavar ", "Press [E] to mine "), -1, -1, PAR_NORMAL, 0, 0, offset_x=-1
                )
            elif f < 180:
                escrever_texto(
                    scr, trd("Aperte [R] para mudar o eixo", "Press [R] to change axis"), -1, -1, PAR_NORMAL, 0, 0
                )
            elif f < 240:
                escrever_texto(
                    scr, trd(" as \"Vidas\" estão no canto superior esquerdo", "Lives are in the upper left corner"), -1, -1, PAR_NORMAL, 0, 0   
                )
            elif f < 285:
                escrever_texto(
                    scr, trd(" as \"Dicas\" estão no canto inferior esquerdo", "Hints are in the lower left corner"), -1, -1, PAR_NORMAL, 0, 0
                )
            elif f < 330:
                escrever_texto(
                    scr, trd(" Ache o tesouro!", "Find the treasure"), -1, -1, PAR_NORMAL, 0, 0, padx=5
                )
            elif f < 380:
                escrever_texto(
                    scr, trd(" Boa sorte!", "Good luck!"), -1, -1, PAR_NORMAL, 0, 0, padx=5
                )
            else:
                set_tutorial_passed(True)


    #! cena opcoes
    def OPCOES(f: int):
        padx:int=15
        key = get_curkey()

        if f == 0:
            mudar_titulo_do_terminal(trd("Opções", "Options"))
            scr.erase()
            y = 0
            escrever_texto(scr, trd("Opções", "Options"), -1, y, PAR_VERMELHO_FUNDO_PRETO, -1, offset_x=3)
        
        if f == 1:
            y = 1
            escrever_texto(scr, trd("OPÇÕES DE LINGUAGEM", "LANGUAGE OPTIONS"), -1, y, PAR_DOURADO_FUNDO_PRETO, 0)
        
        if f == 2:
            y = 2
            escrever_texto(scr, trd("Português", "Portuguese"), -1, y, PAR_NORMAL, 1, padx=padx, offset_x=1)
            escrever_texto(scr, "[1]:", -1, y, PAR_NORMAL, -1, padx=padx, offset_x=1)

        if f == 3:
            y = 3
            escrever_texto(scr, trd("English", "English"), -1, y, PAR_NORMAL, 1, padx=padx, offset_x=1)
            escrever_texto(scr, "[2]:", -1, y, PAR_NORMAL, -1, padx=padx, offset_x=1)

        if f == 5:
            y = 5
            escrever_texto(scr, trd("DADOS", "DATA"), -1, y, PAR_AZUL_FUNDO_PRETO, 0)
        
        if f == 6:
            y = 6
            escrever_texto(scr, trd("Limpar dados", "Clear data"), -1, y, PAR_NORMAL, 1, padx=padx, offset_x=1)
            escrever_texto(scr, "[R]:", -1, y, PAR_NORMAL, -1, padx=padx, offset_x=1)

        if f == 7:
            y = scr.getmaxyx()[0] - 2
            escrever_texto(scr, trd("Voltar", "Back"), -1, y, PAR_VERMELHO_FUNDO_PRETO, 1, padx=padx, offset_x=1)
            escrever_texto(scr, "[3]:", -1, y, PAR_VERMELHO_FUNDO_PRETO, -1, padx=padx, offset_x=1)

        # teclas

        if key == (teclas.DIGIT3): # VOLTAR
            set_scene(1)

        elif key == (teclas.DIGIT1): # PORTUGUES
            set_language(0)
            set_scene(3) # Recarrega a cena para aplicar a tradução

        elif key == (teclas.DIGIT2): # ENGLISH
            set_language(1)
            set_scene(3) # Recarrega a cena para aplicar a tradução

        elif key in [teclas.R, teclas.r]: # REsetar
            armazenamento.limpar()
            set_scene(3)

    #! cena sair
    def SAIR(f: int):
        if f == 0:
            mudar_titulo_do_terminal(trd("Saindo...", "Exiting..."))
            scr.erase()
            escrever_texto(scr, trd("TESOURO  AMAZÔNICO", "AMAZONIC TREASURE HUNT"), -1, 2, PAR_VERDE_FUNDO_PRETO, 0)
            
            escrever_texto(scr, trd("Salvando...", "Saving..."), -1, 4, PAR_NORMAL, 0)
            armazenamento.exportar()
        
        if f == 1:
            escrever_texto(scr, trd("Saindo...", "Exiting..."), -1, 5, PAR_NORMAL, 0)

        if f == 2:
            set_event("scene1_quit")

     
    def VITORIA(f: int):
        key = get_curkey()
        if f == 0:
            mudar_titulo_do_terminal(trd("Vitória!", "Victory!"))
            scr.erase()
        
        if f == 1:
            escrever_texto(scr, trd("VOCÊ VENCEU!", "YOU WIN!"), -1, 2, PAR_DOURADO_FUNDO_PRETO, 0)
    
        if f == 30:
            escrever_texto(scr, trd("Parabéns, você encontrou o tesouro!", "Congratulations, you found the treasure!"), -1, 4, PAR_NORMAL, 0)
    
        if f == 60:
            escrever_texto(scr, trd("[1]: Voltar ao Menu", "[1]: Back to Menu"), -1, 6, PAR_NORMAL, 0)

        if key == (teclas.DIGIT1): # VOLTAR AO MENU
            set_scene(1)

     
    def GAME_OVER(f: int):
        key = get_curkey()
        if f == 0:
            mudar_titulo_do_terminal(trd("Fim de Jogo", "Game Over"))
            scr.erase()
        
        if f == 1:
            escrever_texto(scr, trd("FIM DE JOGO", "GAME OVER"), -1, 2, PAR_VERMELHO_FUNDO_PRETO, 0)
    
        if f == 15:
            escrever_texto(scr, trd("Você ficou sem usos!", "You ran out of uses!"), -1, 4, PAR_NORMAL, 0)
    
        if f == 45:
            escrever_texto(scr, trd("[1]: Voltar ao Menu", "[1]: Back to Menu"), -1, 6, PAR_NORMAL, 0)

        if key == (teclas.DIGIT1): # VOLTAR AO MENU
            set_scene(1)

    [ #! CENAS
        
        # main ->
        TUTORIAL,     # 0

        # TUTORIAL ->
        MENU_INICIAL, # 1

        # MENU_INICIAL ->
        JOGAR,        # 2
        OPCOES,       # 3
        SAIR,         # 4

        # JOGAR ->
        JOGO,         # 5

        # JOGO ->
        VITORIA,      # 6
        GAME_OVER,    # 7

    ][get_scene()](get_frame())
    # ^^^^^^^^^^^  ^^^^^^^^^^^ 
    # |cena atual  |frame atual
# endregion

# region inicio
@on_start.append
def start(stdscr: curses.window):
    curses.resize_term(*get_dimensions())
# endregion

# region quando caractere pressionado
@on_char.append
def char(stdscr: curses.window, char: int):
    if (char in [teclas.ESC]):
        # Se estiver no jogo, volta ao menu. Se não, sai.
        if get_scene() == 5:
            set_scene(1) 
        else:
            set_scene(4)
    
    if (char == curses.KEY_RESIZE):
        curses.resize_term(*get_dimensions())
    
    if (char == curses.KEY_F5) and get_debug():
        set_scene(get_scene())
    
    if (char in [teclas.m, teclas.M]) and get_debug():
        set_scene(1) # Alterado de 0 para 1 para ir ao Menu, não ao Tutorial
    
    if (char in [curses.KEY_F3]):
        set_debug(not get_debug())
        stdscr.erase()
        set_scene(get_scene())

    # A função get_scene() sem argumentos retorna o valor.
    # Para verificar se é a cena 5, use get_scene() == 5
    if (get_scene() == 5):
        x, y = get_x(), get_y()
        if (char in [teclas.a, teclas.A, curses.KEY_LEFT]):
            x = (x - 1)
        elif (char in [teclas.d, teclas.D, curses.KEY_RIGHT]):
            x = (x + 1)
        if (char in [teclas.w, teclas.W, curses.KEY_UP]):
            y = (y - 1)
        elif (char in [teclas.s, teclas.S, curses.KEY_DOWN]):
            y = (y + 1)

        # tratamento de x e y
        maxx, maxy = get_max_pos()
        if (x >= maxx):
            x = 0
        elif (x < 0):
            x = maxx - 1
        if (y >= maxy):
            y = 0
        elif (y < 0):
            y = maxy - 1
        set_x(x)
        set_y(y)

        if (char in [curses.KEY_ENTER, teclas.e, teclas.E, 32]): # Adicionado 32 (Espaço)
            set_event('mine_box')

        if (char in [teclas.R, teclas.r]):
            set_event("change_mode")

    if get_debug():
        if [get_lastkey()] == [curses.KEY_F10]:
            nums = [teclas.DIGIT0, teclas.DIGIT1, teclas.DIGIT2, teclas.DIGIT3, teclas.DIGIT4, teclas.DIGIT5, teclas.DIGIT6, teclas.DIGIT7, teclas.DIGIT8, teclas.DIGIT9]
            if char in nums:
                num = nums.index(char)
                # Proteção para não ir a uma cena que não existe
                if num <= 7: 
                    set_scene(num)
                    set_lastkey(-1)
            return
        
    set_curkey(char)
# endregion

# region main
def main(stdscr: curses.window):

    set_dimensions([12, 48])

    curses.curs_set(0)   # esconde o cursor
    curses.noecho()      # remove o eco das teclas no terminal
    stdscr.nodelay(True)

    for funcao in on_start:
        funcao(stdscr)

    time = sum(os.times())


    while get_running():
        delta = sum(os.times()) - time

        stdscr.timeout(1)
        stdscr.clearok(True)
        char = stdscr.getch()
        if char != teclas.NIL:
            for funcao in on_char:
                funcao(stdscr, char)
        
        for funcao in on_loop:
            funcao(stdscr, delta)

        stdscr.refresh()
        time = delta # CORREÇÃO: 'time' deve ser atualizado para o tempo atual, não 'delta'
        time = sum(os.times()) # Correção do 'time'

        curframe = get_frame() + 1

        #! tratamento de eventos
        if get_event("change_scene"):
            curframe = 0
            set_curkey(-1)
            # curses.flash()

        if get_event("scene1_quit"):
            set_running(False)

        if get_event("resize"):
            set_scene(get_scene())

        if get_event("change_mode"):
            if get_mode() == MODO_X:
                set_mode(MODO_Y)
            else:
                set_mode(MODO_X)

        if get_event("found"):
            curframe = 0
            if get_difficulty() == DIFF_FACIL:
                set_gfacil(True)
            elif get_difficulty() == DIFF_NORMAL:
                set_gmedio(True)
            elif get_difficulty() == DIFF_DIFICIL:
                set_gdificil(True)
            set_scene(6) # Vai para a cena VITORIA

        if get_event("mined"):
            nova_durabilidade = get_durability() - 1
            set_durability(nova_durabilidade)
            if nova_durabilidade <= 0:
                set_event("game_over") 

        if get_event("game_over"):
            curframe = 0
            set_scene(7) # Vai para a cena GAME_OVER

        if get_event("change_notif"):
            set_notif("")

        # Limpa o evento DEPOIS de ser processado
        if get_event() != '': set_event('')
        set_frame(curframe)
        set_curkey(-1)
# endregion

curses.wrapper(main)