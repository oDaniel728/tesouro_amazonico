# PyTTB Terminal

## Sumário
1. [Guia de uso](#guia-de-uso)
2. [Funcionalidades Principais](#funcionalidades-principais)  
2.1. [escreva](#escrevatexto-str)  
2.2. [escreval](#escrevaltexto-str)  
2.3. [atualizar](#atualizar)  
2.5. [pegar_tamanho_do_terminal](#pegar_tamanho_do_terminal---int-int)  
2.6. [mudar_tamanho_do_terminal](#mudar_tamanho_do_terminallargura-int-altura-int)  
2.7. [largura](#largura---int)  
2.8. [altura](#altura---int)  
2.9. [aguardar](#aguardarsegundos-float)  
2.10. [mudar_titulo]

## Guia de uso
Primeiro Passo: Importe o terminal de PyTTB:
```py
from PyTTB import terminal
```
- Agora você já possui todas as funcionalidades do terminal.
---
## Funcionalidades Principais
### `limpar_tela()`
- Limpa a tela do terminal
```python
terminal.limpar_tela()
```
### `escreva(texto: str)`
_`(argumento: tipo)` - `argumento` precisa ser do tipo `tipo`._
- Escreve texto na tela do terminal(mas não atualiza)
```python
terminal.escreva(...)
```
> NOTA: Vale notar que ele não termina com uma quebra de linha(`\n`)

> NOTA: `texto` precisa ser uma string.

> NOTA: `...` pode ser substituido por qualquer coisa, seja criativo :D

### `escreval(texto: str)`
- Escreve texto na tela do terminal(assim como `escreva`), mas ele termina com uma quebra de linha(`\n`)
```python
terminal.escreval(...)
```
### `atualizar()`
- Atualiza o canvas.
```python
terminal.atualizar(...)
```
> NOTA: `escreva(...)` e `escreval(...)` precisam de `.atualizar()` para mostrar as mensagens.

### `pegar_tamanho_do_terminal() -> (int, int)`
_`(...) -> tipo` - função retorna `tipo`_
- Pega o tamanho do terminal no formato `(largura, altura)`.
```py
altura, largura = terminal.pegar_tamanho_do_terminal()
# pega o tamanho do terminal

# ou
tamanho = terminal.pegar_tamanho_do_terminal()
largura = tamanho[0] # primeiro valor
altura = tamanho[1] # segundo valor
```
### `mudar_tamanho_do_terminal(largura: int, altura: int)`
- Muda o tamanho do terminal.
```py
terminal.mudar_tamanho_do_terminal(256, 72)
```
> NOTA: O tamanho do terminal é medido por caracteres, então 1 pixel é `(2, 1)`, sendo 2 caracteres de largura e 1 caractere de altura.
### `largura() -> int`
- Pega a largura do terminal(em caracteres)
```py
largura = terminal.largura()
# ele pega a largura do terminal
```
### `altura() -> int`
- Pega a altura do terminal(em caracteres)
```py
altura = terminal.altura()
# ele pega a altura do terminal.
```
### `aguardar(segundos: float)`
- Aguarda `segundos` segundos.
```py
terminal.aguardar(3)
# ele espera 3 segundos
```

### `mudar_titulo(titulo: str)`
- Muda o titulo da janela, agora sendo `titulo`
```py
terminal.mudar_titulo(...)
# agora titulo é ...
```