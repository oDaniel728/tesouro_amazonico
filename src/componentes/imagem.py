from PyTTB import (canvas as c, tiles)

imagem = \
    c.transformar_tamanho(
        c.criar_imagem("test.png", tiles.fazer_parede(1, 1, 1, 1)),
        (2, 2)
    )

def desenhar():
    c.desenhar(imagem)