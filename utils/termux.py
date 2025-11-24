import os as __os
import sys as __sys
def mudar_titulo_do_terminal(titulo: str) -> None:
    if __os.name == "nt": # windows nt
        __os.system(f"title {titulo}")
    elif __os.name == 'posix': # linux/ macOS
        __sys.stdout.write(f"\x1b]2;{titulo}\x07")
        __sys.stdout.flush()