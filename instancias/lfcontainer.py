# loop function container

import os as __os
from . import fcontainer

_lfcontainer = fcontainer._fcontainer
_function = object

def criar() -> _lfcontainer:
    return []

def adicionar(looper: _lfcontainer, funcao) -> int:
    looper.append(funcao)
    return len(looper)

def executar(looper: _lfcontainer, controller: _function) -> None:
    last_time = sum(__os.times())
    delta = 0

    while bool(controller(delta)): # type: ignore
        for funcao in looper:
            funcao(delta)
    
        current_time = sum(__os.times())
    
        delta = current_time - last_time
    
        last_time = current_time

def remover(looper: _lfcontainer, endereco: int) -> None:
    looper.pop(endereco)

def limpar(looper: _lfcontainer) -> None:
    looper.clear()