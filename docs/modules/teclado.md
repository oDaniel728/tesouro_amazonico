# PyTTB Teclado

## Sumário
1. [Guia de uso](#guia-de-uso)
2. [Funcionalidades Principais](#funcionalidades-principais)  
2.1. [tecla_pressionada](#tecla_pressionada---str--none)

## Guia de uso
Primeiro Passo: Importe o terminal de PyTTB:
```py
from PyTTB import teclado
```
- Agora você já possui todas as funcionalidades do terminal.
---
## Funcionalidades Principais
### `tecla_pressionada() -> str | None`
- Verifica se há uma tecla pressionada no momento, podendo ser `str` ou `None`.
```python
tecla = teclado.tecla_pressionada()
if tecla:
    print(tecla)
```
> NOTA: Recomendo que use dentro de um `while True`
```py
rodando = True
while rodando:
    tecla = teclado.tecla_pressionada()
    if tecla == 'q':
        rodando = False
# fica rodando até que apertar a tecla 'q'
```