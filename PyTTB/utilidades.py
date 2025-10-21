def limitar_inteiro(valor: int, minimo: int, maximo: int) -> int:
    """Limita um valor inteiro entre um intervalo."""
    return max(minimo, min(maximo, valor))