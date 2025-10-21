import typing
eventos = dict[str, list[typing.Callable]]()

def criar_evento(nome: str) -> str:
    eventos.setdefault(nome, [])
    return nome

def remover_evento(nome: str) -> None:
    eventos.pop(nome, None)

def pegar_funcoes_de_evento(nome: str) -> list[typing.Callable]:
    return eventos.get(nome, [])

def conectar_funcao(nome: str, funcao: typing.Callable) -> int:
    func = pegar_funcoes_de_evento(nome)
    func.append(funcao)
    return len(func)

def conectar_uma_vez(nome: str, funcao: typing.Callable) -> int:
    def _f(*args, **kwargs) -> None:
        desconectar_funcao(nome, _f)
        funcao(*args, **kwargs)
    return conectar_funcao(nome, _f)

def desconectar_funcao(nome: str, funcao: typing.Callable) -> None:
    eventos[nome].remove(funcao)

def chamar_evento(nome: str, *args, **kwargs) -> None:
    for funcao in pegar_funcoes_de_evento(nome):
        funcao(*args, **kwargs)

