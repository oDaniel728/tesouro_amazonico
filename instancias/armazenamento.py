from instancias import dicionario
import utils

_chave = str
_valor = object
_pson = str

vars = dicionario.criar()

def criar(nome: _chave, valor: _valor) -> _pson:
    if isinstance(valor, list):
        for v in valor:
            i = valor.index(v)
            dicionario.adicionar(vars, f"{nome}[{i}]", v, False)
    else:
        dicionario.adicionar(vars, nome, valor, False)
    return nome

def remover(nome: _chave) -> None:
    dicionario.remover(vars, nome)

def pegador(nome: _chave, padrao: _valor):
    def _f():
        val = pegar(nome)
        return val if val is not None else padrao
    return _f

def mudador(nome: _chave):
    def _f(v: _valor):
        mudar_valor(nome, v)
    return _f

def estado(nome: _chave, padrao: _valor = None):
    return [pegador(nome, padrao), mudador(nome)]

def pegar(nome: _chave, padrao: _valor = None) -> _valor:
    if not dicionario.chave_existe(vars, nome):
        return padrao
    return dicionario.pegar(vars, nome)

def mudar_valor(nome: _chave, valor: _valor) -> None:
    dicionario.remover(vars, nome)
    dicionario.adicionar(vars, nome, valor)

def possui_valor(nome: _chave) -> bool:
    return dicionario.chave_existe(vars, nome)

def limpar() -> None:
    dicionario.limpar(vars)

def para_texto() -> str:
    r = ''
    for k, v in vars:
        r += f'{k}:{type(v).__name__}={v};\n'
    return r

def exportar() -> None:
    utils.escrever_arquivo(para_texto(), 'vars.pson')

def carregar() -> None:
    if not utils.existe_arquivo('vars.pson'):
        return
    txt = utils.ler_arquivo('vars.pson')
    d = utils.converter.pegar_valor_dicionario(txt)
    for k, v in d:
        dicionario.adicionar(vars, k, v)