from utils.aguarde import aguarde as __aguarde

def para_frame(fps: int, frames: int = 1) -> float:
    return 1 / (fps * frames)

def aguardar_frame(fps: int, frames: int = 1) -> None:
    __aguarde(para_frame(fps, frames))

def criar(fps: int, frames: int = 1):
    def _aguarde():
        aguardar_frame(fps, frames)
    return _aguarde