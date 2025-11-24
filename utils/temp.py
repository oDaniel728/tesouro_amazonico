import os
from .arquivos import escrever_arquivo

pasta = "temp/"

def criar_arquivo(nome: str, conteudo: str) -> str:
    nome_completo = f"./{pasta}{nome}"
    escrever_arquivo(conteudo, nome_completo)
    return nome_completo

def limpar() -> None:
    for f in os.listdir(pasta):
        os.remove(f"{pasta}{f}")

def script_pwsh(conteudo: str) -> str:
    import time

    tmp_id = time.time_ns()  # gera nome único tradicional
    linhas = conteudo.splitlines()

    bloco = "\n".join(linhas)

    return f"""@echo off
setlocal enabledelayedexpansion

set "TMPPS=%temp%\\tmp_script_{tmp_id}.ps1"

> "!TMPPS!" (
{bloco}
)

powershell -NoProfile -File "!TMPPS!"
"""
