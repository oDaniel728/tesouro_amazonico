from PyTTB import (
    terminal as t,
    canvas as c,
    teclado as kb,
    eventos as e,
    data,
    atalhos,
    tiles,
    audio
)

from . import componentes

c.redimensionar(32, 16)
AO_SAIR = e.criar_evento("ao_sair")
rodando = True

@atalhos.tecla_pressionada("q")
def _quando_tecla_q_pressionada():
    audio.tocar_audio("audio.wav")
    global rodando; rodando = False


def renderizar_tela():
    c.apagar_canvas()  # limpa frame anterior
    componentes.tela_inicial.desenhar()
    componentes.imagem.desenhar()
    c.atualizar()  # escreve canvas

def loop_principal():
    while rodando:
        renderizar_tela()
        atalhos.verificar_atalhos()
        t.aguardar(1/60)
loop_principal()

e.chamar_evento(AO_SAIR)
