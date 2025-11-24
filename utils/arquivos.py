import os
import sys

def escrever_arquivo(texto: str, caminho: str) -> None:
    fd = os.open(caminho, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    os.write(fd, texto.encode(sys.getdefaultencoding()))
    os.close(fd)

def ler_arquivo(caminho: str) -> str:
    fd = os.open(caminho, os.O_RDONLY)
    conteudo = b""
    while True:
        parte = os.read(fd, 1024)
        if not parte:
            break
        conteudo += parte
    os.close(fd)
    return conteudo.decode(sys.getdefaultencoding())

def deletar_arquivo(caminho: str) -> None:
    if os.path.exists(caminho) and not os.path.isdir(caminho):
        os.remove(caminho)

def criar_pasta(caminho: str) -> None:
    if not os.path.exists(caminho):
        os.makedirs(caminho)

def remover_pasta(caminho: str) -> None:
    if os.path.isdir(caminho):
        os.rmdir(caminho)

def existe_arquivo(caminho: str) -> bool:
    return os.path.exists(caminho)

def pegar_pasta(caminho: str) -> list[str]:
    return os.listdir(caminho) if os.path.isdir(caminho) else []

def e_pasta(caminho: str) -> bool:
    return os.path.isdir(caminho)
