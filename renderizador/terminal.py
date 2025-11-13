import sys as __sys
from ._aguarde import aguarde as __aguarde

# region SETUP

cursor_escondido = False
delay: float = 0
auto_atualizar = False
def __aguardar() -> None:
    if delay != 0:
        __aguarde(delay)
def configurar(_delay: float = 0, _auto_atualizar: bool = False) -> None:
    global delay, auto_atualizar
    delay = _delay
    auto_atualizar = _auto_atualizar

# endregion

# region FUNÇÕES BÁSICAS

def escreva(texto: str, _atualizar: bool | None = None) -> None: 
    __sys.stdout.write(texto) 
    if _atualizar is None: _atualizar = auto_atualizar
    if _atualizar: atualizar() 
    __aguardar()

def escreval(texto: str, _atualizar: bool | None = None) -> None: 
    escreva(texto + "\n", _atualizar) 

def atualizar() -> None: 
    __sys.stdout.flush()

def limpar(_atualizar: bool | None = None) -> None: 
    escreva("\x1b[2J", _atualizar) 

# endregion

# region POSIÇÕES

def ir_em(em: list[int]) -> None:
    """Move o cursor para a posição [linha, coluna]."""
    escreva(f"\x1b[{em[0]};{em[1]}H")

def escreva_em(texto: str, em: list[int], _atualizar: bool | None = None) -> None:
    """Escreve um texto na posição [linha, coluna]."""
    ir_em(em)
    escreva(texto, _atualizar)

def limpar_em(em: list[int], _atualizar: bool | None = None) -> None:
    """Limpa o caractere na posição [linha, coluna]."""
    ir_em(em)
    escreva(" ", _atualizar)

# endregion

# region CURSOR

def esconder_cursor() -> None:
    """Esconde o cursor do terminal."""
    global cursor_escondido
    escreva("\x1b[?25l")
    cursor_escondido = True
    atualizar()

def mostrar_cursor() -> None:
    """Mostra o cursor do terminal."""
    global cursor_escondido
    escreva("\x1b[?25h")
    cursor_escondido = False
    atualizar()

# endregion


# region TAMANHO_TERMINAL
import os as __os
def pegar_tamanho_do_terminal():
    return __os.get_terminal_size(1).columns, __os.get_terminal_size(1).lines

def mudar_tamanho_do_terminal(linhas: int, colunas: int) -> None:
    __os.system(f"mode con cols={colunas} lines={linhas}")

def limpar_e_mudar_tamanho_do_terminal(linhas: int, colunas: int) -> None:
    limpar()
    mudar_tamanho_do_terminal(linhas, colunas)

# endregion