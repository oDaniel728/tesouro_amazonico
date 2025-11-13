_fcontainer = list
_fendereco = int
_fretorno = list[object]

def criar() -> _fcontainer:
    return []

def adicionar(looper: _fcontainer, funcao) -> _fendereco:
    looper.append(funcao)
    return len(looper)

def remover(looper: _fcontainer, endereco: _fendereco) -> None:
    looper.pop(endereco)

def executar(looper: _fcontainer) -> _fretorno:
    r = []
    for funcao in looper:
        r.append(funcao())
    return r

def executador(looper: _fcontainer):
    def _executar() -> _fretorno:
        return executar(looper)
    return _executar