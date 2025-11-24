def centralizar_largura(texto: str, largura: int) -> int:
    return (largura - len(texto)) // 2
def centralizar_altura(texto: str, altura: int) -> int:
    return (altura - len(texto.splitlines())) // 2