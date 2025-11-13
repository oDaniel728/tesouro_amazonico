from random import randint as __randint


_posicao = list[int]
_posicaof = list[float]
def criar(x: int, y: int | None = None) -> _posicao:
    return [x, y or x]

def criarf(x: float, y: float | None = None) -> _posicaof:
    return [x, y or x]

def x(posicao: _posicao) -> int:
    return posicao[0]
def y(posicao: _posicao) -> int:
    return posicao[1]
def xf(posicao: _posicaof) -> float:
    return posicao[0]
def yf(posicao: _posicaof) -> float:
    return posicao[1]

def somar(pos1: _posicao, pos2: _posicao) -> _posicao:
    return criar(
        x(pos1) + x(pos2),
        y(pos1) + y(pos2)
    )

def sub(pos1: _posicao, pos2: _posicao) -> _posicao:
    return criar(
        x(pos1) + x(pos2),
        y(pos1) + y(pos2)
    )

def mult(pos1: _posicaof, pos2: _posicaof) -> _posicaof:
    return criarf(
        xf(pos1) * xf(pos2),
        yf(pos1) * yf(pos2)
    )

def div(pos1: _posicaof, pos2: _posicaof) -> _posicaof:
    return criarf(
        xf(pos1) / xf(pos2),
        yf(pos1) / yf(pos2)
    )

def operar(pos1: _posicao, pos2: _posicao, func) -> _posicao:
    return func(pos1, pos2)

def aleatorio(pos1: _posicao, pos2: _posicao) -> _posicao:
    return criar(
        __randint(x(pos1), x(pos2)),
        __randint(y(pos1), y(pos2))
    )