import tkinter as tk
from typing import TypeAlias
from .plugins import tiles
from .terminal import pegar_cor_de_caractere

rgb: TypeAlias = tuple[int, int, int]
rgba: TypeAlias = tuple[int, int, int, int]
rgba_map: TypeAlias = list[list[rgba]]
rgbchar_map: TypeAlias = list[list[tuple[rgb, str]]]
canvas_table: TypeAlias = dict[tuple[int, int], str]


def carregar_imagem(caminho: str) -> rgba_map:
    """Carrega uma imagem PNG em matriz RGBA."""
    root = tk.Tk()
    root.withdraw()  # oculta janela
    img = tk.PhotoImage(file=caminho, master=root)

    largura, altura = img.width(), img.height()
    matriz: rgba_map = []
    for y in range(altura):
        linha = []
        for x in range(largura):
            valores = img.get(x, y)
            if len(valores) == 3:
                valores = (*valores, 255)
            linha.append(valores)
        matriz.append(linha)

    root.destroy()  # libera recursos
    return matriz

alpha_map = ( dict[tuple[int, int], str] ) \
(   # {(min, max) : char}
    {
        (0, 16): tiles.fazer_parede_cheia(5),
        (17, 64): tiles.fazer_parede_cheia(4),
        (65, 128): tiles.fazer_parede_cheia(3),
        (128, 176): tiles.fazer_parede_cheia(2),
        (177, 255): tiles.fazer_parede_cheia(1)
    }
)
def _pegar_alpha_map(alpha: int) -> str:
    for (min, max), char in alpha_map.items():
        if min <= alpha <= max:
            return char
    return ' '

def converter_rgba_map(matriz: rgba_map) -> rgbchar_map:
    """Converte RGBA para par (RGB, caractere)."""
    resultado: rgbchar_map = []
    for linha in matriz:
        nova = []
        for r, g, b, a in linha:
            nova.append(((r, g, b), _pegar_alpha_map(a)))
        resultado.append(nova)
    return resultado

def colorir_texto(rgb: rgb, texto: str) -> str:
    """Aplica cor ao texto retornando string formatada."""
    return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{texto}\033[0m"

def converter_em_canvas_table(
    matriz: rgbchar_map, proporcao: tuple[int, int] = (2, 1),
    char: str | None = None
) -> canvas_table:
    """Converte matriz em dicionário {(x, y): caractere colorido}, aplicando proporção."""
    escala_x, escala_y = proporcao
    tabela: canvas_table = {}
    for y, linha in enumerate(matriz):
        for x, (rgb, ch) in enumerate(linha):
            cor = colorir_texto(rgb, ch if not char else char)
            for dy in range(escala_y):
                for dx in range(escala_x):
                    if pegar_cor_de_caractere(cor) == (0, 0, 0): continue
                    tabela[(x * escala_x + dx, y * escala_y + dy)] = cor
    return tabela

def imagem_para_canvas_map(caminho: str, char: str | None = None, proporcao: tuple[int, int] = (2, 1)) -> canvas_table:
    """Cria uma imagem a partir de um caminho e retorna como dicionário de pontos."""
    rgba = carregar_imagem(caminho)
    rgbchar = converter_rgba_map(rgba)
    return converter_em_canvas_table(rgbchar, proporcao, char)