import importlib.util
import os
from typing import Callable, ParamSpec, TypeVar

def carregar_componentes(pasta: str) -> tuple[Callable, Callable]:
    setups: list[Callable] = []
    loops: list[Callable] = []

    for arquivo in os.listdir(pasta):
        if not arquivo.endswith(".py"):
            continue

        caminho = os.path.join(pasta, arquivo)
        nome_modulo = os.path.splitext(arquivo)[0]

        spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
        if spec is None or spec.loader is None:
            continue

        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)

        if hasattr(modulo, "setup") and callable(modulo.setup):
            setups.append(modulo.setup)
        if hasattr(modulo, "loop") and callable(modulo.loop):
            loops.append(modulo.loop)

    def _setups():
        for setup in setups:
            setup()

    def _loops():
        for loop in loops:
            r = loop()
            if r == -1:
                loops.remove(loop)
    return _setups, _loops

P = ParamSpec("P")
R = TypeVar("R")
def chamar(funcoes: list[Callable[P, R]], *args: P.args, **kwargs: P.kwargs) -> list[R]:
    r = []
    for funcao in funcoes:
        r.append(funcao(*args, **kwargs))

    return r