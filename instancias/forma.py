from curses import window as __window
from . import dicionario

_forma = dicionario._dicionario

def criar() -> _forma:
    return dicionario.criar()

def adicionar_ponto(forma: _forma, posicao: list[int], ponto: str) -> None:
    dicionario.adicionar(forma, posicao, ponto, False)

def adicionar_pontos(forma: _forma, posicoes: list, ponto: str) -> None:
    for posicao in posicoes:
        adicionar_ponto(forma, posicao, ponto) # type: ignore

def desenhar(forma: _forma, janela: __window, attr: int = 0) -> None:
    for pos, char in forma:
        janela.addstr(pos[1], pos[0], char, attr)

def pegar(forma: _forma, posicao: list[int], padrao: str | None = ' ') -> str | None:
    return dicionario.pegar(forma, posicao, padrao) # type: ignore