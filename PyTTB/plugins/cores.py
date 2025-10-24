rgb_color = tuple[int, int, int]

def rgb_to_hex(rgb: rgb_color) -> str:
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
def hex_to_rgb(hex: str) -> rgb_color:
    return (int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:7], 16))
def colorir_texto(rgb: rgb_color, text: str) -> str:
    return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text}\033[0m"

def somar_rgb(rgb1: rgb_color, rgb2: rgb_color) -> rgb_color:
    r = min(255, max(0, rgb1[0] + rgb2[0]))
    g = min(255, max(0, rgb1[1] + rgb2[1]))
    b = min(255, max(0, rgb1[2] + rgb2[2]))
    return (r, g, b)

def somar_hex(hex1: str, hex2: str) -> str:
    rgb1 = hex_to_rgb(hex1)
    rgb2 = hex_to_rgb(hex2)
    return rgb_to_hex(somar_rgb(rgb1, rgb2))

def subtrair_rgb(rgb1: rgb_color, rgb2: rgb_color) -> rgb_color:
    r = min(255, max(0, rgb1[0] - rgb2[0]))
    g = min(255, max(0, rgb1[1] - rgb2[1]))
    b = min(255, max(0, rgb1[2] - rgb2[2]))
    return (r, g, b)

def subtrair_hex(hex1: str, hex2: str) -> str:
    rgb1 = hex_to_rgb(hex1)
    rgb2 = hex_to_rgb(hex2)
    return rgb_to_hex(subtrair_rgb(rgb1, rgb2))

def brilhar_rgb(rgb: rgb_color, brilho: int) -> rgb_color:
    r = min(255, max(0, rgb[0] + brilho))
    g = min(255, max(0, rgb[1] + brilho))
    b = min(255, max(0, rgb[2] + brilho))
    return (r, g, b)

def brilhar_hex(hex: str, brilho: int) -> str:
    rgb = hex_to_rgb(hex)
    return rgb_to_hex(brilhar_rgb(rgb, brilho))

def media_rgb(rgb1: rgb_color, rgb2: rgb_color) -> rgb_color:
    r = (rgb1[0] + rgb2[0]) // 2
    g = (rgb1[1] + rgb2[1]) // 2
    b = (rgb1[2] + rgb2[2]) // 2
    return (r, g, b)

def media_hex(hex1: str, hex2: str) -> str:
    rgb1 = hex_to_rgb(hex1)
    rgb2 = hex_to_rgb(hex2)
    return rgb_to_hex(media_rgb(rgb1, rgb2))