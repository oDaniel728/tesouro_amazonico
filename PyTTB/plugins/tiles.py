shade_full = '█'
shade_dark = '▓'
shade_medium = '▒'
shade_light = '░'
shade_void = ' '

def fazer_parede(topo_esq: int, topo_dir: int, baixo_esq: int, baixo_dir: int) -> str:
    return dict[tuple[int, int, int, int], str]({
        (0, 0, 0, 0): shade_void,
        (0, 0, 0, 1): '▗',
        (0, 0, 1, 0): '▖',
        (0, 0, 1, 1): '▄',
        (0, 1, 0, 0): '▝',
        (0, 1, 0, 1): '▐',
        (0, 1, 1, 0): '▞',
        (0, 1, 1, 1): '▟',
        (1, 0, 0, 0): '▘',
        (1, 0, 0, 1): "▚",
        (1, 0, 1, 0): "▌",
        (1, 0, 1, 1): "▙",
        (1, 1, 0, 0): "▀",
        (1, 1, 0, 1): "▜",
        (1, 1, 1, 0): "▛",
        (1, 1, 1, 1): shade_full,
    }).get((topo_esq, topo_dir, baixo_esq, baixo_dir), shade_full)

def fazer_parede_cheia(transparencia: int = 1) -> str:
    """Faz uma parede cheia:
    Args:
        transparencia (int, optional): Transparencia da parede. Defaults to 1.\n
            1: 100%  
            2: 75%  
            3: 50%  
            4: 25%  
            5: 0%  
    """
    return dict[int, str]({
        1: shade_full,
        2: shade_dark,
        3: shade_medium,
        4: shade_light,
        5: shade_void
    }).get(transparencia, shade_full)

def fazer_braile(a: int, b: int, c: int, d: int, e: int, f: int) -> str:
    # estrutura do braile:
    # a d
    # b e
    # c f
    # 1: Aceso, 0: Apagado

    # Mapeamento de bits conforme a tabela Unicode Braille (U+2800)
    # Posições:
    # 1 4
    # 2 5
    # 3 6
    codigo = (
        (a << 0) |  # ponto 1
        (b << 1) |  # ponto 2
        (c << 2) |  # ponto 3
        (d << 3) |  # ponto 4
        (e << 4) |  # ponto 5
        (f << 5)    # ponto 6
    )

    return chr(0x2800 + codigo)
