import sys
buffer = list[list[str]]()

def escrever_buffer(buffer: list[list[str]] = buffer):
    sys.stdout.write("\033[H")  # move cursor pro topo
    for linha in buffer:
        sys.stdout.write("".join(linha))