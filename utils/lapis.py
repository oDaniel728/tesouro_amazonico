import curses as __curses

BAIXO = ESQUERDA = -1
MEIO  = CENTRO   = 0
CIMA  = DIREITA  = 1

def escrever_texto(stdscr: __curses.window, txt: str, x: int, y: int,
                   attr: int = 0, alinhamento_h: int = ESQUERDA,
                   alinhamento_v: int = CIMA,
                   offset_x: int = 0, offset_y: int = 0,
                   padx: int = 0, pady: int = 0) -> None:

    h, w = stdscr.getmaxyx()
    linhas = txt.splitlines()
    total_linhas = len(linhas)

    # -1 => borda
    if x < 0 and alinhamento_h != ESQUERDA:
        x = w + x
    if y < 0 and alinhamento_v != CIMA:
        y = h + y

    # alinhamento horizontal
    if alinhamento_h == MEIO:
        x = (w // 2) - (len(txt) // 2)
    elif alinhamento_h == DIREITA:
        x = x - len(txt)

    # alinhamento vertical
    if alinhamento_v == MEIO:
        y = (h // 2) - (total_linhas // 2)
    elif alinhamento_v == BAIXO:
        y -= total_linhas

    # aplicar offset + padding
    if alinhamento_h == ESQUERDA:
        x += offset_x + padx
    elif alinhamento_v == DIREITA:
        x += offset_x - padx

    if alinhamento_v == CIMA:
        y += offset_y + pady
    elif alinhamento_v == BAIXO:
        y += offset_y - pady
    

    # clamp
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x >= w:
        x = w - 1
    if y >= h:
        y = h - 1

    stdscr.addstr(y, x, txt.replace("\0", ""), attr)
