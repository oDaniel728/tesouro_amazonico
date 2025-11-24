import curses as __curses

# tipos
_cor4_id = int
_par     = int

# contador
__ID = [0]

# cache: [(r,g,b,id)]
__CORES = []          # cores já criadas
# cache: [(fg,bg,id,attr)]
__PARES = []          # pares já criados

def __rgb_1000(n: int) -> int:
    return n * 1000 // 255


def criar(r: int, g: int, b: int) -> _cor4_id:
    # procura em cache
    for R, G, B, ID in __CORES:
        if R == r and G == g and B == b:
            return ID

    # cria nova
    novo_id = __ID[0] + 1
    __curses.init_color(novo_id,
        __rgb_1000(r),
        __rgb_1000(g),
        __rgb_1000(b)
    )
    __ID[0] = novo_id

    __CORES.append([r, g, b, novo_id])
    return novo_id


rgb = criar

def rgba(r: int, g: int, b: int, a: int) -> _cor4_id:
    return criar(r, g, b)


def criar_hex(hexstr: str) -> _cor4_id:
    if hexstr.startswith("#"):
        hexstr = hexstr[1:]
    r = int(hexstr[0:2], 16)
    g = int(hexstr[2:4], 16)
    b = int(hexstr[4:6], 16)
    return criar(r, g, b)


def criar_par(fg: _cor4_id, bg: _cor4_id = __curses.COLOR_BLACK) -> _par:
    # procura par existente
    for F, B, ID, ATTR in __PARES:
        if F == fg and B == bg:
            return ATTR

    novo_id = __ID[0] + 1
    __curses.init_pair(novo_id, fg, bg)
    __ID[0] = novo_id

    attr = __curses.color_pair(novo_id)
    __PARES.append([fg, bg, novo_id, attr])
    return attr
