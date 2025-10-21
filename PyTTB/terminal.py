from typing import TypeVar; _T = TypeVar("_T")

from .utilidades import limitar_inteiro
import os

tamanho = None

def rodar_comando(windows: str, linux: str | None = None):
    """Executa um comando no terminal."""

    linux = linux or windows
    os.system(windows if os.name == "nt" else linux)

def limpar_tela():
    """Limpa a tela do terminal."""

    rodar_comando(windows="cls", linux="clear")

def escreva(texto: str):
    """Escreve texto sem pular linha."""
    
    print(texto, end='', flush=False)

def escreval(texto: str):
    """Escreve texto e pula uma linha."""
    
    escreva(texto + "\n")

def atualizar():
    """Força atualização do terminal (flush)."""
    
    print('', end='', flush=True)

def leia(tipo: type[_T]) -> _T:
    """Lê entrada do usuário e converte para o tipo informado.
    Em caso de erro, repete a leitura.
    """
    
    entrada = input()
    try:
        return tipo(entrada) # type: ignore
    
    except:
        escreval(f"{VERMELHO}[{RESET}ERRO{VERMELHO}]{RESET}: {VERMELHO_CLARO}Entrada inválida! {RESET}")
        return leia(tipo)
    
def pegar_tamanho_do_terminal() -> tuple[int, int]:
    """Retorna o tamanho do terminal (largura, altura)."""
    
    if tamanho: return tamanho
    return os.get_terminal_size()

def largura() -> int:
    """Retorna a largura do terminal."""
    
    return pegar_tamanho_do_terminal()[0]

def altura() -> int:
    """Retorna a altura do terminal."""
    
    return pegar_tamanho_do_terminal()[1]

def mudar_tamanho_do_terminal(colunas: int, linhas: int):
    """Muda o tamanho do terminal."""
    
    # max_cols, max_lns = pegar_tamanho_do_terminal()

    # colunas = limitar_inteiro(colunas, 1, max_cols)
    # linhas = limitar_inteiro(linhas, 1, max_lns)

    # if colunas == -1: colunas = max_cols
    # if linhas == -1: linhas = max_lns
    
    global tamanho; tamanho = (colunas, linhas)
    rodar_comando(f"mode con cols={colunas} lines={linhas}", "printf '\033[8;40;100t'")

def aguardar(segundos: float):
    """Simula time.sleep(segundos) usando busy-wait."""
    
    tempo_inicial = sum(os.times())
    while (sum(os.times()) - tempo_inicial) < segundos:
        pass

def mudar_titulo(titulo: str):
    """Muda o título do terminal."""
    
    rodar_comando(f"title {titulo}", f"echo -ne '\033]0;{titulo}\007'")

# Cores de texto (foreground)
PRETO    = FG_BLACK   = "\033[30m"
VERMELHO = FG_RED     = "\033[31m"
VERDE    = FG_GREEN   = "\033[32m"
AMARELO  = FG_YELLOW  = "\033[33m"
AZUL     = FG_BLUE    = "\033[34m"
MAGENTA  = FG_MAGENTA = "\033[35m"
CIANO    = FG_CYAN    = "\033[36m"
BRANCO   = FG_WHITE   = "\033[37m"

# Cores brilhantes
PRETO_CLARO    = FG_BRIGHT_BLACK   = "\033[90m"
VERMELHO_CLARO = FG_BRIGHT_RED     = "\033[91m"
VERDE_CLARO    = FG_BRIGHT_GREEN   = "\033[92m"
AMARELO_CLARO  = FG_BRIGHT_YELLOW  = "\033[93m"
AZUL_CLARO     = FG_BRIGHT_BLUE    = "\033[94m"
MAGENTA_CLARO  = FG_BRIGHT_MAGENTA = "\033[95m"
CIANO_CLARO    = FG_BRIGHT_CYAN    = "\033[96m"
BRANCO_CLARO   = FG_BRIGHT_WHITE   = "\033[97m"

# Cores de fundo (background)
FUNDO_PRETO    = BG_BLACK   = "\033[40m"
FUNDO_VERMELHO = BG_RED     = "\033[41m"
FUNDO_VERDE    = BG_GREEN   = "\033[42m"
FUNDO_AMARELO  = BG_YELLOW  = "\033[43m"
FUNDO_AZUL     = BG_BLUE    = "\033[44m"
FUNDO_MAGENTA  = BG_MAGENTA = "\033[45m"
FUNDO_CIANO    = BG_CYAN    = "\033[46m"
FUNDO_BRANCO   = BG_WHITE   = "\033[47m"

# Efeitos de formatação
RESET       = "\033[0m"
NEGRITO     = "\033[1m"
FRACO       = "\033[2m"
ITALICO     = "\033[3m"
SUBLINHADO  = "\033[4m"
PISCANDO    = "\033[5m"
INVERTIDO   = "\033[7m"
OCULTO      = "\033[8m"

def colorir_texto(cor: str | tuple[int, int, int], texto: str):
    """Aplica cor ao texto retornando string formatada."""
    
    if isinstance(cor, tuple): cor = fgcor_rgb(*cor)
    elif cor.startswith("#"): cor = fgcor_hex(cor)

    return f"{cor}{texto}{RESET}"
def colorir_fundo(cor: str | tuple[int, int, int], texto: str):
    """Aplica cor ao fundo retornando string formatada."""
    
    if isinstance(cor, tuple): cor = bgcor_rgb(*cor)
    elif cor.startswith("#"): cor = bgcor_hex(cor)

    return f"{cor}{texto}{RESET}"

ctex = colorir_texto
cfun = colorir_fundo

_paleta = dict(
    R=RESET,
    FGR=FG_RED,
    FGG=FG_GREEN,
    FGB=FG_BLUE,
    FGY=FG_YELLOW,
    FGM=FG_MAGENTA,
    FGC=FG_CYAN,
    FGBR=FG_BRIGHT_RED,
    FGBG=FG_BRIGHT_GREEN,
    FGBB=FG_BRIGHT_BLUE,
    FGBY=FG_BRIGHT_YELLOW,
    FGBM=FG_BRIGHT_MAGENTA,
    FGBC=FG_BRIGHT_CYAN,
    BGR=BG_RED,
    BGGB=BG_GREEN,
    BGBB=BG_BLUE,
    BGBY=BG_YELLOW,
    BGBM=BG_MAGENTA,
    BGBC=BG_CYAN,
    B=NEGRITO,
    W=FRACO,
    I=ITALICO,
    S=SUBLINHADO,
    P=PISCANDO,
    N=INVERTIDO
)

def formatar(texto: str, cores: dict[str, str] = _paleta, formato: str = '[{}]'):
    """Substitui códigos de cores e efeitos no texto pelo ANSI correspondente."""
    
    for cor in cores:
        texto = texto.replace(formato.format(cor), cores[cor])
    
    return texto

def fgcor_rgb(r: int, g: int, b: int) -> str:
    """Retorna ANSI escape code para cor de foreground RGB."""
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    return f"\033[38;2;{r};{g};{b}m"

def bgcor_rgb(r: int, g: int, b: int) -> str:
    """Retorna ANSI escape code para cor de background RGB."""
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    return f"\033[48;2;{r};{g};{b}m"

def fgcor_hex(hex_code: str) -> str:
    """Recebe código hex (#RRGGBB ou RRGGBB) e retorna ANSI escape code para foreground."""
    hex_code = hex_code.lstrip('#')
    r, g, b = int(hex_code[0:2], 16), int(hex_code[2:4], 16), int(hex_code[4:6], 16)
    return fgcor_rgb(r, g, b)

def bgcor_hex(hex_code: str) -> str:
    """Recebe código hex (#RRGGBB ou RRGGBB) e retorna ANSI escape code para background."""
    hex_code = hex_code.lstrip('#')
    r, g, b = int(hex_code[0:2], 16), int(hex_code[2:4], 16), int(hex_code[4:6], 16)
    return bgcor_rgb(r, g, b)
