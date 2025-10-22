import sys
import os
import subprocess

# Windows
if sys.platform == "win32":
    import winsound

    def tocar_audio(caminho: str, volume: float = 1.0) -> str:
        """
        Toca um áudio WAV de forma assíncrona (sem abrir programas).
        O volume é apenas simbólico em Windows (winsound não suporta controle direto).
        """
        volume = max(0.0, min(volume, 1.0))
        winsound.PlaySound(caminho, winsound.SND_FILENAME | winsound.SND_ASYNC)
        return "winsound"

    def parar_audio(_id: str) -> None:
        """Para qualquer áudio tocando."""
        winsound.PlaySound(None, winsound.SND_PURGE)

# Linux / macOS
else:
    _processos: dict[int, subprocess.Popen] = {}

    def tocar_audio(caminho: str, volume: float = 1.0) -> int:
        """
        Toca áudio WAV/MP3 via utilitário do sistema (aplay/afplay).
        volume varia entre 0.0 e 1.0.
        """
        volume = max(0.0, min(volume, 1.0))
        if sys.platform.startswith("linux"):
            proc = subprocess.Popen(
                ["aplay", caminho],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        else:  # macOS
            proc = subprocess.Popen(
                ["afplay", caminho, "-v", str(volume)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        _processos[proc.pid] = proc
        return proc.pid

    def parar_audio(pid: int) -> None:
        """Encerra o áudio tocando."""
        proc = _processos.pop(pid, None)
        if proc and proc.poll() is None:
            proc.terminate()
