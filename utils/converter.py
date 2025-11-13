
from instancias import dicionario


def parse_valor(txt: str):
    txt = txt.strip()

    if txt.lower() in ("true", "false"):
        return txt.lower() == "true"
    if txt == "None":
        return None

    # número inteiro
    if txt.isdigit() or (txt.startswith("-") and txt[1:].isdigit()):
        return int(txt)

    # número decimal
    try:
        return float(txt)
    except ValueError:
        pass

    # lista simples separada por vírgula
    if txt.startswith("[") and txt.endswith("]"):
        conteudo = txt[1:-1].strip()
        if not conteudo:
            return []
        return [parse_valor(x.strip()) for x in conteudo.split(",")]

    # dicionário básico
    if txt.startswith("{") and txt.endswith("}"):
        conteudo = txt[1:-1].strip()
        if not conteudo:
            return {}
        pares = [x.split(":", 1) for x in conteudo.split(",")]
        return {p[0].strip(" '\""): parse_valor(p[1].strip()) for p in pares}

    # string normal
    return txt.strip("'\"")

def pegar_valor(txt: str):
    #formato = "nome:tipo=valor;"
    valor = txt.split("=", 1)[1].strip(";").strip("'\"").strip()

    return valor

def pegar_nome(txt: str) -> str:
    return txt.split(":", 1)[0].strip()

def pegar_tipo(txt: str):
    t = txt.split(":", 1)[1].split("=", 1)[0].strip()
    return t

def _lista_pegar_item(txt: str) -> str:
    # formato: lista[item]:tipo=valor;
    item = txt.split("[", 1)[1].split("]", 1)[0]
    return item
def _lista_pegar_nome_completo(txt: str) -> str:
    # formato: lista[item]:tipo=valor;
    nome_completo = txt.split(":", 1)[0]
    return nome_completo
def _lista_pegar_nome(txt: str) -> str:
    # formato: lista[item]:tipo=valor;
    nome_lista = txt.split("[",1)[0]
    return nome_lista
def _lista_e_lista(txt: str) -> bool:
    # formato: <nome>[<item>]:<T>=<V>;
    nome_completo = _lista_pegar_nome_completo(txt)
    return nome_completo.__contains__("[") and nome_completo.__contains__("]")
def _lista_nome_de_lista(txt: str) -> bool:
    return '[' in txt and ']' in txt

def _get_indentation(txt: str, size: int = 4) -> int:
    count = 0
    for c in txt:
        if c == " ":
            count += 1
        else:
            break
    return count // size


def _add_indentation(txt: str, tabs: int = 1, size: int = 4) -> str:
    tabs = tabs * size
    indent = " " * tabs
    linhas = txt.splitlines()
    return "\n".join(indent + linha if linha.strip() else linha for linha in linhas)

def pegar_valor_primitivo(txt: str) -> object:
    t = pegar_tipo(txt)
    v = pegar_valor(txt)
    r = None

    if t == 'int':
        r = int(v)
    elif t == 'str':
        r = str(v)
    elif t == 'float':
        r = float(v)
    elif t == 'bool':
        r = bool(v)
    elif t == 'list':
        r = []

    elif t == 'dicionario':
        r = []

    return r

def pegar_valor_dicionario(txt: str) -> dicionario._dicionario:
    returning = dicionario.criar()
    get_returning, set_returning = dicionario.estado(returning)
    linhas = txt.replace("\n", "").split(";")
    
    for linha in linhas:
        if linha.strip() == "":
            continue
        nome = pegar_nome(linha)
        tipo = pegar_tipo(linha)
        valor = pegar_valor_primitivo(linha)
        if _lista_nome_de_lista(nome):
            nomel = _lista_pegar_nome(linha)
            set_returning(nomel, [], False)
            item = _lista_pegar_item(linha)
            i: list = get_returning(nomel, []) # type: ignore
            i.insert(int(item), pegar_valor_primitivo(linha))
            set_returning(nomel, i)
        else:
            set_returning(nome, pegar_valor_primitivo(linha))

    return returning