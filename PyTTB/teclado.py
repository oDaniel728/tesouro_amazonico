import sys

# Windows
if sys.platform == "win32":
    import msvcrt

    def tecla_pressionada():
        """Verifica se alguma tecla foi pressionada."""
        if msvcrt.kbhit():          # tecla foi pressionada?
            return msvcrt.getch().decode("utf-8", errors="ignore")
        return None

# Linux / macOS
else:
    import termios, tty, select

    def tecla_pressionada():
        """Verifica se alguma tecla foi pressionada."""
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)  # modo não-bloqueante
            dr, dw, de = select.select([sys.stdin], [], [], 0)
            if dr:
                return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return None