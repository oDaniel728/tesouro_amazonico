from typing import Callable, overload
from .. import eventos
from .. import teclado

atalhos = dict[str, str]()
estado_teclas: dict[str, bool] = dict()  # True = pressionada, False = liberada

def adicionar_atalho(tecla: str) -> str:
    atalhos.setdefault(tecla, eventos.criar_evento(f"tecla_{tecla}"))
    estado_teclas.setdefault(tecla, False)
    return tecla
    
def pegar_atalho(tecla: str) -> str:
    adicionar_atalho(tecla)
    return atalhos[tecla]

def remover_atalho(tecla: str) -> None:
    eventos.remover_evento(pegar_atalho(tecla))
    atalhos.pop(tecla)
    estado_teclas.pop(tecla, None)

@overload
def tecla_pressionada(tecla: str, /) -> Callable: ...
@overload
def tecla_pressionada(tecla: str, funcao: Callable) -> None: ...

def tecla_pressionada(tecla: str, funcao: Callable | None = None) -> Callable | None:
    if funcao:
        eventos.conectar_funcao(pegar_atalho(tecla), funcao)
    else:
        def wrapper(funcao: Callable) -> None:
            eventos.conectar_funcao(pegar_atalho(tecla), funcao)
        return wrapper

def desconectar_atalho(tecla: str, funcao: Callable) -> None:
    eventos.desconectar_funcao(pegar_atalho(tecla), funcao)

def chamar_atalho(tecla: str, *args, **kwargs) -> None:
    eventos.chamar_evento(pegar_atalho(tecla), *args, **kwargs)

_tecla_solta   = dict[str, list[Callable]]()
_tecla_ativada = dict[str, list[Callable]]()

@overload
def tecla_solta(tecla: str, /) -> Callable: ...
@overload
def tecla_solta(tecla: str, funcao: Callable) -> None: ...

def tecla_solta(tecla: str, funcao: Callable | None = None) -> Callable | None:
    if funcao:
        _tecla_solta.setdefault(tecla, []).append(funcao)
    else:
        def wrapper(funcao: Callable) -> None:
            _tecla_solta.setdefault(tecla, []).append(funcao)
        return wrapper

@overload
def tecla_ativada(tecla: str, /) -> Callable: ...
@overload
def tecla_ativada(tecla: str, funcao: Callable) -> None: ...

def tecla_ativada(tecla: str, funcao: Callable | None = None) -> Callable | None:
    if funcao:
        _tecla_ativada.setdefault(tecla, []).append(funcao)
    else:
        def wrapper(funcao: Callable) -> None:
            _tecla_ativada.setdefault(tecla, []).append(funcao)
        return wrapper

def verificar_atalhos():
    tecla_atual = teclado.tecla_pressionada()

    for tecla in atalhos.keys():
        pressionada_antes = estado_teclas.get(tecla, False)
        pressionada_agora = tecla == tecla_atual

        # pressed
        if pressionada_agora and not pressionada_antes:
            chamar_atalho(tecla)
            # activated dispara imediatamente se a tecla estiver pressionada
            for f in _tecla_ativada.get(tecla, []):
                f()

        # released
        if not pressionada_agora and pressionada_antes:
            for f in _tecla_solta.get(tecla, []):
                f()

        # atualizado o estado
        estado_teclas[tecla] = pressionada_agora

def esperar_por_tecla(tecla: str):
    while teclado.tecla_pressionada() != tecla:
        verificar_atalhos()
