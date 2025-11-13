from .terminal import *
from ..instancias import buffer

# region DBUFFERING
__w, __h = pegar_tamanho_do_terminal()
__front = buffer.criar(__w, __h)
__back = buffer.criar(__w, __h)

def dbuff_swap():
    global __front, __back
    __front, __back = __back, __front

def renderizar_front(_atualizar: bool | None = None):
    dbuff_swap()
    escreva(buffer.para_string(__front), _atualizar)

# endregion

def desenhar(dicionario: buffer._dicionario) -> None:
    buffer.adicionar_dicionario(__back, dicionario)

def desenhar_ponto(posicao: list[int], ponto: str) -> None:
    buffer.adicionar_ponto(__back, posicao, ponto)

def pegar_dicionario(ignorar: list[str] = [' ']) -> buffer._dicionario:
    return buffer.pegar_dicionario(__back, ignorar)

def limpar():
    buffer.limpar(__back)