import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def escreva(texto: str):
    print(texto, end='', flush=False)

def escreval(texto: str):
    escreva(texto + "\n")

def atualizar_tela():
    print('', end='', flush=True)

def leia(tipo: type):
    m = input()
    try:
        return tipo(m)
    except:
        escreval(f"{VERMELHO}[{RESET}ERRO{VERMELHO}]{RESET}: {VERMELHO_CLARO}Entrada inválida! {RESET}")
        return leia(tipo)

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

def colorir_texto(cor: str, texto: str):
    return f"{cor}{texto}{RESET}"

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
    NE=NEGRITO,
    FR=FRACO,
    IT=ITALICO,
    SL=SUBLINHADO,
    PI=PISCANDO,
    IN=INVERTIDO
)

def formatar(texto: str, cores: dict[str, str] = _paleta, formato: str = '[{}]'):
    for cor in cores:
        texto = texto.replace(formato.format(cor), cores[cor])
    return texto