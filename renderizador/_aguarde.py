import os

def aguarde(s: float) -> None:
    """Aguarda um tempo em segundos"""
    def pegar_tempo() -> float:
        return sum(os.times())
    alvo = s
    inicio = pegar_tempo()

    while ((pegar_tempo()) - inicio) < alvo:
        pass