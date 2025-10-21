import typing
eventos = dict[str, list[typing.Callable]]()

def criar_evento(nome: str) -> str:
    """Cria um evento e retorna o seu endereço"""
    eventos.setdefault(nome, [])
    return nome

def remover_evento(nome: str) -> None:
    """Remove um evento"""
    eventos.pop(nome, None)

def pegar_funcoes_de_evento(nome: str) -> list[typing.Callable]:
    """Retorna uma lista com as funções conectadas ao evento"""
    return eventos.get(nome, [])

def conectar_funcao(nome: str, funcao: typing.Callable) -> int:
    """Conecta uma função ao evento"""
    func = pegar_funcoes_de_evento(nome)
    func.append(funcao)
    return len(func)

def conectar_uma_vez(nome: str, funcao: typing.Callable) -> int:
    """Conecta uma função ao evento e desconecta quando ela for chamada"""
    def _f(*args, **kwargs) -> None:
        desconectar_funcao(nome, _f)
        funcao(*args, **kwargs)
    return conectar_funcao(nome, _f)

def desconectar_funcao(nome: str, funcao: typing.Callable) -> None:
    """Desconecta uma função do evento"""
    eventos[nome].remove(funcao)

def chamar_evento(nome: str, *args, **kwargs) -> None:
    """Chama um evento"""
    for funcao in pegar_funcoes_de_evento(nome):
        funcao(*args, **kwargs)

