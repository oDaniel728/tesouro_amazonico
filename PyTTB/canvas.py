from . import terminal as t
from . import imagens as img
from math import sqrt

Vector2D = tuple[int, int]
canvas_points: dict[Vector2D, str] = {}
PREENCHER = "_P"

redimensionar = t.mudar_tamanho_do_terminal

def somar_vetores(vetor1: Vector2D, vetor2: Vector2D) -> Vector2D:
    """Soma dois vetores 2D e retorna o resultado."""
    return (vetor1[0] + vetor2[0], vetor1[1] + vetor2[1])

def porporcao_vetores(vetor1: Vector2D, vetor2: Vector2D = (2, 1)) -> Vector2D:
    """Multiplica dois vetores 2D e retorna o resultado."""
    return (vetor1[0] * vetor2[0], vetor1[1] * vetor2[1])

def pegar_centro(vetor: Vector2D) -> Vector2D:
    """Retorna o centro de um vetor 2D."""
    return (vetor[0] // 2, vetor[1] // 2)

def vec2d(x: int | str, y: int | str) -> Vector2D:
    """Retorna um vetor 2D. Se x ou y forem PREENCHER ou str, usa o tamanho do terminal."""
    largura, altura = t.pegar_tamanho_do_terminal()
    return ((largura if isinstance(x, str) or x == PREENCHER else x),
            (altura if isinstance(y, str) or y == PREENCHER else y))
criar_vector2d = vec2d

def pegar_x(vetor: Vector2D) -> int:
    """Retorna o valor do eixo X de um vetor 2D."""
    return vetor[0]

def pegar_y(vetor: Vector2D) -> int:
    """Retorna o valor do eixo Y de um vetor 2D."""
    return vetor[1]

def limpar_canvas():
    """Limpa o terminal utilizando a função de terminal."""
    t.limpar_tela()

def apagar_canvas():
    """Remove todos os pontos do canvas."""
    canvas_points.clear()

def apagar(pontos: dict[Vector2D, str] | list[tuple[Vector2D, str]]):
    """Remove pontos específicos do canvas, podendo ser dict ou lista de pontos."""
    if isinstance(pontos, dict):
        for posicao in pontos.keys():
            canvas_points.pop(posicao, None)
    else:
        for posicao, _ in pontos:
            canvas_points.pop(posicao, None)

def gerar_canvas_lista() -> list[list[str]]:
    """Retorna o canvas completo como uma lista 2D de caracteres."""
    largura, altura = t.pegar_tamanho_do_terminal()
    canvas_2d: list[list[str]] = []
    for y in range(altura):
        linha = []
        for x in range(largura):
            linha.append(canvas_points.get((x, y), ' '))
        canvas_2d.append(linha)
    return canvas_2d

# ======= CRIAR FORMAS =======

def criar_ponto(posicao: Vector2D, caractere: str) -> dict[Vector2D, str]:
    """Cria um ponto e retorna como dicionário de posições e caracteres."""
    x, y = posicao
    return {(x, y): caractere}

def criar_linha(pos_inicial: Vector2D, pos_final: Vector2D, caractere: str) -> dict[Vector2D, str]:
    """Cria uma linha entre dois pontos e retorna como dicionário de posições e caracteres."""
    x1, y1 = pos_inicial
    x2, y2 = pos_final
    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)
    passo_x = 1 if x1 < x2 else -1
    passo_y = 1 if y1 < y2 else -1
    erro = delta_x - delta_y
    tabela: dict[Vector2D, str] = {}
    while True:
        tabela[(x1, y1)] = caractere
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * erro
        if e2 > -delta_y:
            erro -= delta_y
            x1 += passo_x
        if e2 < delta_x:
            erro += delta_x
            y1 += passo_y
    return tabela

def criar_retangulo(pos_inicial: Vector2D, pos_final: Vector2D, borda: str, preenchimento: str | bool | None = None) -> dict[Vector2D, str]:
    """Cria um retângulo com borda e opcional preenchimento e retorna como dicionário de pontos."""
    tabela: dict[Vector2D, str] = {}
    x1, y1 = pos_inicial
    x2, y2 = pos_final
    for x in range(min(x1, x2), max(x1, x2)+1):
        for y in range(min(y1, y2), max(y1, y2)+1):
            if x in (x1, x2) or y in (y1, y2):
                tabela[(x, y)] = borda
            elif preenchimento:
                if preenchimento == True:
                    preenchimento = borda
                tabela[(x, y)] = preenchimento
    return tabela

def criar_circulo(centro: Vector2D, raio: int, borda: str, preenchimento: str | None = None) -> dict[Vector2D, str]:
    """Cria um círculo com borda e opcional preenchimento e retorna como dicionário de pontos."""
    tabela: dict[Vector2D, str] = {}
    cx, cy = centro
    for y in range(cy - raio, cy + raio + 1):
        for x in range(cx - raio, cx + raio + 1):
            distancia = sqrt((x - cx)**2 + (y - cy)**2)
            if abs(distancia - raio) < 0.5:
                tabela[(x, y)] = borda
            elif preenchimento and distancia < raio:
                tabela[(x, y)] = preenchimento
    return tabela

def criar_elipse(centro: Vector2D, raio_x: int, raio_y: int, borda: str, preenchimento: str | None = None) -> dict[Vector2D, str]:
    """Cria uma elipse com borda e opcional preenchimento e retorna como dicionário de pontos."""
    tabela: dict[Vector2D, str] = {}
    cx, cy = centro
    for y in range(cy - raio_y, cy + raio_y + 1):
        for x in range(cx - raio_x, cx + raio_x + 1):
            dx = (x - cx) / raio_x
            dy = (y - cy) / raio_y
            valor = dx*dx + dy*dy
            if 0.9 <= valor <= 1.1:
                tabela[(x, y)] = borda
            elif preenchimento and valor < 1:
                tabela[(x, y)] = preenchimento
    return tabela

def criar_texto(pos_inicial: Vector2D, texto: str) -> dict[Vector2D, str]:
    """Cria um texto como tabela de pontos a partir da posição inicial."""
    tabela: dict[Vector2D, str] = {}
    x, y = pos_inicial
    for i, caractere in enumerate(texto):
        tabela[(x + i, y)] = caractere
    return tabela

def criar_linhas(pontos: list[Vector2D], caractere: str) -> dict[Vector2D, str]:
    """Cria uma série de linhas conectando os pontos em sequência (polilinha)."""
    tabela: dict[Vector2D, str] = {}
    for i in range(len(pontos) - 1):
        tabela.update(criar_linha(pontos[i], pontos[i + 1], caractere))
    return tabela

def criar_imagem(caminho: str, char: str | None = None) -> dict[Vector2D, str]:
    """Cria uma imagem a partir de um caminho e retorna como dicionário de pontos."""
    return img.imagem_para_canvas_map(caminho, char)

# ======= DESENHAR FORMAS =======

def desenhar(tabela: dict[Vector2D, str], deslocamento: Vector2D = (0, 0)):
    """Desenha uma tabela de pontos no canvas, aplicando um deslocamento opcional."""
    for posicao, caractere in tabela.items():
        canvas_points[somar_vetores(posicao, deslocamento)] = caractere
desenhar_forma = desenhar

def desenhar_ponto(posicao: Vector2D, caractere: str):
    """Cria e desenha um ponto no canvas."""
    tabela = criar_ponto(posicao, caractere)
    desenhar_forma(tabela)
    return list(tabela.keys())

def desenhar_linha(pos_inicial: Vector2D, pos_final: Vector2D, caractere: str):
    """Cria e desenha uma linha no canvas."""
    tabela = criar_linha(pos_inicial, pos_final, caractere)
    desenhar_forma(tabela)
    return list(tabela.keys())

def desenhar_retangulo(pos_inicial: Vector2D, pos_final: Vector2D, borda: str, preenchimento: str | None = None):
    """Cria e desenha um retângulo no canvas."""
    tabela = criar_retangulo(pos_inicial, pos_final, borda, preenchimento)
    desenhar_forma(tabela)
    return list(tabela.keys())

def desenhar_circulo(centro: Vector2D, raio: int, borda: str, preenchimento: str | None = None):
    """Cria e desenha um círculo no canvas."""
    tabela = criar_circulo(centro, raio, borda, preenchimento)
    desenhar_forma(tabela)
    return list(tabela.keys())

def desenhar_elipse(centro: Vector2D, raio_x: int, raio_y: int, borda: str, preenchimento: str | None = None):
    """Cria e desenha uma elipse no canvas."""
    tabela = criar_elipse(centro, raio_x, raio_y, borda, preenchimento)
    desenhar_forma(tabela)
    return list(tabela.keys())

def desenhar_texto(pos_inicial: Vector2D, texto: str):
    """Cria e desenha um texto no canvas."""
    tabela = criar_texto(pos_inicial, texto)
    desenhar_forma(tabela)
    return list(tabela.keys())

def desenhar_linhas(pontos: list[Vector2D], caractere: str):
    """Cria e desenha linhas conectando uma lista de pontos (polilinha)."""
    tabela = criar_linhas(pontos, caractere)
    desenhar_forma(tabela)
    return list(tabela.keys())

def desenhar_imagem(caminho: str):
    """Cria e desenha uma imagem no canvas."""
    tabela = criar_imagem(caminho)
    desenhar_forma(tabela)
    return list(tabela.keys())

def atualizar():
    """Renderiza todo o canvas no terminal linha por linha."""
    canvas = gerar_canvas_lista()
    conteudo = "\n".join("".join(linha) for linha in canvas)
    t.escreva("\n" + conteudo)
    t.atualizar()

# Vetor2
def _maior_vetor(forma: dict[Vector2D, str]) -> Vector2D:
    """Retorna o maior ponto da forma."""
    vec = (0, 0)
    for posicao in forma.keys():
        if posicao[0] > vec[0]:
            vec = (posicao[0], vec[1])
        if posicao[1] > vec[1]:
            vec = (vec[0], posicao[1])
    return vec

def _menor_vetor(forma: dict[Vector2D, str]) -> Vector2D:
    """Retorna o menor ponto da forma."""
    vec = _maior_vetor(forma)
    for posicao in forma.keys():
        if posicao[0] < vec[0]:
            vec = (posicao[0], vec[1])
        if posicao[1] < vec[1]:
            vec = (vec[0], posicao[1])
    return vec

def _delta_vetor(v1: Vector2D, v2: Vector2D) -> Vector2D:
    """Retorna o delta entre dois vetores."""
    x = abs(v1[0] - v2[0])
    y = abs(v1[1] - v2[1])
    return (x, y)

def area_da_forma(forma: dict[Vector2D, str]) -> Vector2D:
    """Retorna a area da forma."""
    return _maior_vetor(forma)

def transformar_deslocamento(forma: dict[Vector2D, str], deslocamento: Vector2D) -> dict[Vector2D, str]:
    """Desloca uma forma."""
    tabela: dict[Vector2D, str] = {}
    for posicao, caractere in forma.items():
        tabela[somar_vetores(posicao, deslocamento)] = caractere
    return tabela

def transformar_tamanho(forma: dict[Vector2D, str], aumento: Vector2D) -> dict[Vector2D, str]:
    """Aumenta uma forma proporcionalmente no eixo X e Y."""
    ax, ay = aumento
    nova_forma: dict[Vector2D, str] = {}
    for (x, y), ch in forma.items():
        for dy in range(ay):
            for dx in range(ax):
                nova_forma[(x * ax + dx, y * ay + dy)] = ch
    return nova_forma

def transformar(forma: dict[Vector2D, str], deslocamento: Vector2D = (0, 0), aumento: Vector2D = (1, 1)) -> dict[Vector2D, str]:
    """Desloca e aumenta uma forma."""
    return transformar_tamanho(transformar_deslocamento(forma, deslocamento), aumento)