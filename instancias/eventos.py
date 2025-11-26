_evento = list
_func = object
_evento_atual = []

def criar(nome: str = "__main__") -> _evento:
    return [nome]

def acionar(evento: _evento | str) -> None:
    if isinstance(evento, str):
        evento = [evento]
    _evento_atual.extend(evento)

def pegar() -> _evento:
    return _evento_atual

def evento_e(nome: str | _evento):
    evento = nome in _evento_atual
    if isinstance(nome, str):
        if nome in _evento_atual:
            _evento_atual.remove(nome)
            return True
    elif isinstance(nome, list):
        for n in nome:
            if n in _evento_atual:
                _evento_atual.remove(n)
    return evento

def limpar() -> None:
    _evento_atual.clear()