_estado = list

_getter = object
_setter = object

def criar(vi: object = 0) -> _estado:
    valor: list[object] = [vi]
    def getter():
        return valor[0]
    def setter(v: object) -> None:
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