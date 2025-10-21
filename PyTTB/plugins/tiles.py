upper_half = '▀'
lower_half = '▄'
left_half = '▌'
right_half = '▐'
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