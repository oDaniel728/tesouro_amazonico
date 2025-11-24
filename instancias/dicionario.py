"""

### Dicionarios
- Dicionarios são uma estrutura de dados que armazena pares de chave e valor.
Uteis para armazenar dados em uma forma pareada e organizada.
---
(importe como: `import dicionario`, mas pode mudar dependendo do seu projeto)
- Para criar um dicionário, use:  
```
    dic = dicionario.criar()
```
> _Isso cria uma pseudo-instância de um dicionario._

- Para adicionar uma chave ao dicionário, use:
```
    dicionario.adicionar(dic, chave, valor)
```
> _Isso adiciona a chave ao dicionario._

- Para pegar o valor de uma chave, use:
```
    dicionario.pegar(dic, chave)
```
> _Isso retorna o valor da chave._

- Para remover uma chave do dicionario, use:
```
    dicionario.remover(dic, chave)
```
> _Isso remove a chave do dicionario._

- Para limpar um dicionario, use:
```
    dicionario.limpar(dic)
```
> _Isso limpa o dicionario._

- Para verificar se uma chave existe no dicionario, use:
```
    dicionario.chave_existe(dic, chave)
```
> _Isso retorna True se a chave existir no dicionario._
"""

_chave = object
_valor = object
_dicionario = list

def criar() -> _dicionario:
    """Cria uma pseudo-instância de um dicionario

    Returns:
        _dicionario: instância de um dicionario
    """
    return []

def criar_getter(dicionario: _dicionario):
    def _f(chave: str, default: object):
        return pegar(dicionario, chave, default)
    return _f

def criar_setter(dicionario: _dicionario):
    def _f(chave: str, valor: object, sobre_escrever: bool = True):
        if not sobre_escrever and chave_existe(dicionario, chave): return
        adicionar(dicionario, chave, valor)
    return _f

def estado(dicionario: _dicionario):
    return criar_getter(dicionario), criar_setter(dicionario)

def adicionar(dicionario: _dicionario, chave: _chave, valor: _valor, remover_duplicatas: bool = True):
    """diciona uma chave ao dicionário e atribui o seu valo

    Args:
        dicionario (_dicionario): instância de um dicionario
        chave (_chave): chave, termo
        valor (_valor): valor, signifcado
    """
    if remover_duplicatas:
        if chave_existe(dicionario, chave):
            remover(dicionario, chave)
    dicionario.append([chave, valor])


def pegar(dicionario: _dicionario, chave: _chave, padrao: _valor = None) -> _valor:
    """ega o valor de uma chave de um dicionari

    Args:
        dicionario (_dicionario): instância de um dicionario
        chave (_chave): chave, termo
        padrao (_valor, optional): valor padrão, caso não exista no dicionario. None por padrão.

    Returns:
        _valor | None: valor, signifcado; caso não exista, retorna o padrão
    """
    for item in dicionario:
        chave_, valor_ = item
        if chave_ == chave:
            return valor_
    return padrao

def remover(dicionario: _dicionario, chave: _chave) -> _dicionario:
    """emove uma chave de um dicionari

    Args:
        dicionario (_dicionario): instância de um dicionario
        chave (_chave): chave que deseja remover

    Returns:
        _dicionario: instância de um dicionario
    """
    for item in dicionario:
        chave, _ = item
        if chave == chave:
            dicionario.remove(item)
            break
    return dicionario

def limpar(dicionario: _dicionario) -> _dicionario:
    """impa um dicionari

    Args:
        dicionario (_dicionario): instância de um dicionario

    Returns:
        _dicionario: instância de um dicionario
    """
    dicionario.clear()
    return dicionario


def chave_existe(dicionario: _dicionario, chave: _chave) -> bool:
    """erifica se há uma chave em um dicionari

    Args:
        dicionario (_dicionario): instância de um dicionario
        chave (_chave): chave que você está verificando

    Returns:
        bool: se ela existe
    """
    for item in dicionario:
        k, _ = item
        if k == chave:
            return True
    return False

def quantidade(dicionario: _dicionario) -> int:
    """erifica o número de chaves em um dicionari

    Args:
        dicionario (_dicionario): instância de um dicionario

    Returns:
        int: número de chaves
    """
    return len(dicionario)

def chaves(dicionario: _dicionario) -> list[_chave]:
    """Retorna as chaves de um dicionario

    Args:
        dicionario (_dicionario): instância de um dicionario

    Returns:
        list[_chave]: chaves
    """
    chave = []
    for item in dicionario:
        chave.append(item[0])
    return chave

def valores(dicionario: _dicionario) -> list[_valor]:
    """Retorna os valores de um dicionario

    Args:
        dicionario (_dicionario): instância de um dicionario

    Returns:
        list[_valor]: valores
    """
    valor = []
    for item in dicionario:
        valor.append(item[1])
    return valor

def juntar(dicionario1: _dicionario, dicionario2: _dicionario) -> _dicionario:
    """junta dois dicionarios

    Args:
        dicionario1 (_dicionario): instância de um dicionario
        dicionario2 (_dicionario): instância de um dicionario

    Returns:
        _dicionario: instância de um dicionario
    """
    d = criar()
    for chave, valor in dicionario1:
        adicionar(d, chave, valor)
    for chave, valor in dicionario2:
        adicionar(d, chave, valor)
    return d