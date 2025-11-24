from typing import Callable


_estado = list

_getter = object
_setter = object

def criar(vi: object = 0, quando_mudado: Callable[[object, object], None] | None = None) -> _estado:
    valor: list[object] = [vi]
    def getter(v: object = None):
        if v:
            return valor[0] == v
        return valor[0]
    def setter(v: object) -> None:
        if quando_mudado: quando_mudado(valor, v)
        valor[0] = v
    return [getter, setter]

def getter(estado: _estado):
    def __getter() -> object:
        return estado[0]()
    return __getter

def setter(estado: _estado):
    def __setter(v: object) -> None:
        estado[1](v)
    return __setter

def get(estado: _estado) -> object:
    return getter(estado)()

def set(estado: _estado, v: object) -> None:
    setter(estado)(v)

def gset(estado: _estado):
    return getter(estado), setter(estado)