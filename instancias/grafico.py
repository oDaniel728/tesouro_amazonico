from . import dicionario
from . import posicao

_grafico = dicionario._dicionario

def criar() -> _grafico:
    return dicionario.criar()

def adicionar(graf: _grafico, ponto: posicao._posicao, char: str) -> _grafico:
    dicionario.adicionar(graf, ponto, char)
    return graf

def pegar(graf: _grafico, ponto: posicao._posicao, padrao: str = ' ') -> str:
    return str(dicionario.pegar(graf, ponto, padrao))

def limpar(graf: _grafico) -> _grafico:
    return dicionario.limpar(graf)

def juntar(graf1: _grafico, graf2: _grafico) -> _grafico:
    return dicionario.juntar(graf1, graf2)