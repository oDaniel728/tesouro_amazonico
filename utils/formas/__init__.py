import math
from instancias import forma as _forma

_pontos = _forma._forma

#region Criar

def c_reta(x1: int, y1: int, x2: int, y2: int, char: str =' '):
    f = _forma.criar()

    dx = abs(x2 - x1)
    dy = -abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx + dy

    while True:
        _forma.adicionar_ponto(f, [x1, y1], char)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x1 += sx
        if e2 <= dx:
            err += dx
            y1 += sy

    return f



def c_retangulo(x1: int, y1: int, x2: int, y2: int, char: str =' ', preenchimento: str | None =None, attr: int | None =None):
    f = _forma.criar()
    xmin, xmax = sorted([x1, x2])
    ymin, ymax = sorted([y1, y2])

    for x in range(xmin, xmax + 1):
        _forma.adicionar_ponto(f, [x, ymin], char)
        _forma.adicionar_ponto(f, [x, ymax], char)

    for y in range(ymin, ymax + 1):
        _forma.adicionar_ponto(f, [xmin, y], char)
        _forma.adicionar_ponto(f, [xmax, y], char)

    if preenchimento:
        p = char if preenchimento is True else preenchimento
        for x in range(xmin + 1, xmax):
            for y in range(ymin + 1, ymax):
                _forma.adicionar_ponto(f, [x, y], p)

    return f

def c_circulo(x: int, y: int, r: int, char: str =' ', preenchimento: str | None | bool =None, attr: int | None =None):
    f = _forma.criar()
    for ang in range(0, 360):
        rad = math.radians(ang)
        px = x + round(r * math.cos(rad))
        py = y + round(r * math.sin(rad))
        _forma.adicionar_ponto(f, [px, py], char)

    if preenchimento:
        p = char if preenchimento is True else preenchimento
        for px in range(x - r, x + r + 1):
            for py in range(y - r, y + r + 1):
                if (px - x) ** 2 + (py - y) ** 2 <= r * r:
                    _forma.adicionar_ponto(f, [px, py], p)

    return f

def c_elipse(x1: int, y1: int, x2: int, y2: int, char: str =' ', preenchimento: str | None | bool =None, attr: int | None =None):
    f = _forma.criar()
    a = abs(x2 - x1) / 2
    b = abs(y2 - y1) / 2
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2

    for ang in range(0, 360):
        rad = math.radians(ang)
        px = round(cx + a * math.cos(rad))
        py = round(cy + b * math.sin(rad))
        _forma.adicionar_ponto(f, [px, py], char)

    if preenchimento:
        p = char if preenchimento is True else preenchimento
        for px in range(int(cx - a), int(cx + a + 1)):
            for py in range(int(cy - b), int(cy + b + 1)):
                if ((px - cx) ** 2) / (a * a) + ((py - cy) ** 2) / (b * b) <= 1:
                    _forma.adicionar_ponto(f, [px, py], p)

    return f

def c_pontos(pontos: _pontos, char: str =' ', preenchimento: str | None | bool=None, attr: int | None =None):
    f = _forma.criar()
    for x, y in pontos:
        _forma.adicionar_ponto(f, [x, y], char)
    return f

AH_ESQUERDA = AV_CIMA   = -1
AH_CENTRO   = AV_CENTRO =  0
AH_DIREITA  = AV_BAIXO  =  1

def c_texto(
    x1: int, y1: int, x2: int, y2: int,
    texto: str,
    alinhamento_h: int = AH_CENTRO,
    alinhamento_v: int = AV_CENTRO,
    attr=None
):
    f = _forma.criar()

    # cálculo da posição base
    if alinhamento_h == AH_ESQUERDA:
        x_base = x1
    elif alinhamento_h == AH_CENTRO:
        x_base = (x1 + x2) // 2
    else:  # AH_DIREITA
        x_base = x2

    if alinhamento_v == AV_CIMA:
        y_base = y1
    elif alinhamento_v == AV_CENTRO:
        y_base = (y1 + y2) // 2
    else:  # AV_BAIXO
        y_base = y2

    # render centralizado por largura real do texto
    inicio_x = x_base - len(texto) // 2

    for i, ch in enumerate(texto):
        px = inicio_x + i
        py = y_base

        # checagem de barreira
        if px < x1 or px > x2:
            continue
        if py < y1 or py > y2:
            continue

        _forma.adicionar_ponto(f, [px, py], ch)

    return f

#endregion

#region Editar

def e_deslocar(forma, x, y):
    f = _forma.criar()
    for pos, char in forma:
        _forma.adicionar_ponto(f, [pos[0] + x, pos[1] + y], char)
    return f

def e_rotacionar(forma, angulo):
    f = _forma.criar()
    rad = math.radians(angulo)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)

    for pos, char in forma:
        x, y = pos
        xr = round(x * cos_a - y * sin_a)
        yr = round(x * sin_a + y * cos_a)
        _forma.adicionar_ponto(f, [xr, yr], char)

    return f

def e_escalar(forma, x, y):
    f = _forma.criar()
    for pos, char in forma:
        xs = round(pos[0] * x)
        ys = round(pos[1] * y)
        _forma.adicionar_ponto(f, [xs, ys], char)
    return f

#endregion

#region Modelar

def m_unir(formas):
    f = _forma.criar()
    for fo in formas:
        for pos, char in fo:
            _forma.adicionar_ponto(f, pos, char)
    return f

def m_negar(forma1, forma2):
    f = _forma.criar()
    for pos, char in forma1:
        if _forma.pegar(forma2, pos, None) is None:
            _forma.adicionar_ponto(f, pos, char)
    return f

def m_intersecao(forma1, forma2):
    f = _forma.criar()
    for pos, char in forma1:
        if _forma.pegar(forma2, pos, None) is not None:
            _forma.adicionar_ponto(f, pos, char)
    return f

#endregion

#region Utilidades

u_desenhar = _forma.desenhar

#endregion