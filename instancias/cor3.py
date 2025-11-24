_cor3 = list[int]
_hex = str
_R = int
_G = int
_B = int

def criar(r: _R, g: _G, b: _B) -> _cor3:
    return [r, g, b]

def para_hex(cor: _cor3) -> _hex:
    return f'#{cor[0]:02x}{cor[1]:02x}{cor[2]:02x}'

def criar_hex(hex: _hex) -> _cor3:
    if hex.startswith('#'): hex = hex[1:] # descarta o #
    return criar(
        int(hex[0:2], 16), # RR .. .. .*
        int(hex[2:4], 16), # .. GG .. .*
        int(hex[4:6], 16)  # .. .. BB .*
    )

def red(cor: _cor3 | _hex) -> _R:
    if isinstance(cor, str): # if type(cor) == str:
        cor = criar_hex(cor)
        return cor[0]
    else:
        return cor[0]
    
def green(cor: _cor3 | _hex) -> _G:
    if isinstance(cor, str): # if type(cor) == str:
        cor = criar_hex(cor)
        return cor[1]
    else:
        return cor[1]
    
def blue(cor: _cor3 | _hex) -> _B:
    if isinstance(cor, str): # if type(cor) == str:
        cor = criar_hex(cor)
        return cor[2]
    else:
        return cor[2]