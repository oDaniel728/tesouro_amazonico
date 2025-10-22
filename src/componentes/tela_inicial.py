from PyTTB import (canvas as c, tiles)

tela_inicial = c.criar_retangulo(
    (0, 0),
    (31, 15),
    c.t.ctex("#1f5d16ff", tiles.fazer_parede(1, 1, 1, 1)),
    c.t.ctex("#389629ff", tiles.fazer_parede(1, 1, 1, 1)),
)

def desenhar():
    c.desenhar(tela_inicial)