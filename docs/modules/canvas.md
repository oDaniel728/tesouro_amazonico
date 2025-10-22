# PyTTB Canvas

## Sumário
- [Guia de uso](#guia-de-uso)
- [Funções de Vetores](#funções-de-vetores)
- [Canvas](#canvas)
- [Criação de Formas](#criação-de-formas)
- [Desenhar Formas](#desenhar-formas)
- [Atualização](#atualização)

## Guia de uso
Primeiro passo: Importe o módulo canvas de PyTTB:
```python
from PyTTB import canvas
````

* Você terá acesso a vetores, canvas e funções de desenho no terminal.

---

## Funções de Vetores

### `vec2d(x: int | str, y: int | str) -> tuple[int, int]`

* Retorna um vetor 2D. Se `x` ou `y` forem `"_P"` ou `str`, usa o tamanho do terminal.

```python
v = canvas.vec2d(10, "_P")
```

### `somar_vetores(v1, v2) -> tuple[int, int]`

* Soma dois vetores 2D.

```python
v3 = canvas.somar_vetores((1,2), (3,4)) # retorna (4,6)
```

### `pegar_x(vetor) -> int`

* Retorna o valor X do vetor.

```python
x = canvas.pegar_x((5, 7)) # 5
```

### `pegar_y(vetor) -> int`

* Retorna o valor Y do vetor.

```python
y = canvas.pegar_y((5, 7)) # 7
```

### `pegar_centro(vetor) -> tuple[int, int]`

* Retorna o centro do vetor (divisão por 2).

```python
centro = canvas.pegar_centro((10, 6)) # (5,3)
```

---

## Canvas

### `limpar_canvas()`

* Limpa o terminal.

```python
canvas.limpar_canvas()
```

### `apagar_canvas()`

* Remove todos os pontos do canvas.

```python
canvas.apagar_canvas()
```

### `apagar(pontos)`

* Remove pontos específicos do canvas (dict ou lista de tuplas).

```python
canvas.apagar({(1,1): "X"})
```

### `gerar_canvas_lista() -> list[list[str]]`

* Retorna o canvas completo como lista 2D.

```python
lista_canvas = canvas.gerar_canvas_lista()
```

---

## Criação de Formas

Todas as funções retornam `dict[tuple[int,int], str]` representando os pontos da forma.

### `criar_linha(pos_inicial, pos_final, caractere)`

* Cria uma linha entre dois pontos.

```python
linha = canvas.criar_linha((0,0), (5,5), "*")
```

### `criar_retangulo(pos_inicial, pos_final, borda, preenchimento=None)`

* Cria retângulo com borda e opcional preenchimento.

```python
ret = canvas.criar_retangulo((1,1), (4,3), "#", ".")
```

### `criar_circulo(centro, raio, borda, preenchimento=None)`

* Cria círculo.

```python
circ = canvas.criar_circulo((5,5), 3, "O", ".")
```

### `criar_elipse(centro, raio_x, raio_y, borda, preenchimento=None)`

* Cria elipse.

```python
elip = canvas.criar_elipse((5,5), 4, 2, "E", "-")
```

### `criar_texto(pos_inicial, texto)`

* Cria texto como pontos.

```python
txt = canvas.criar_texto((0,0), "Olá")
```

### `criar_linhas(pontos, caractere)`

* Cria uma forma conectando os pontos.

```python
pol = canvas.criar_linhas([(0,0),(1,2),(3,3)], "*")
```

### `criar_imagem(caminho: str, caractere: str?, proporcao: Vector2D?)`

* Transforma a imagem do `caminho` em um tabela para ser desenhada.
> `caractere` por padrão é a transparência por pixel.
> `porporcao` por padrão é `(2, 1)`

```python
imagem = criar_imagem("imagem.png")
```

---

## Desenhar Formas

As funções desenham diretamente no canvas e retornam lista de posições.

### `desenhar(tabela, deslocamento=(0,0))`

* Desenha tabela de pontos aplicando deslocamento.

```python
canvas.desenhar({(1,1): "X"}, (2,2))
```

### Funções prontas para formas:

* `desenhar_linha(...)`
* `desenhar_retangulo(...)`
* `desenhar_circulo(...)`
* `desenhar_elipse(...)`
* `desenhar_texto(...)`
* `desenhar_linhas(...)`
* `desenhar_imagem(...)`

Exemplo:

```python
canvas.desenhar_retangulo((1,1),(5,3),"#",".")
```

---

## Atualização

### `atualizar()`

* Renderiza todo o canvas no terminal.

```python
canvas.atualizar()
```

> NOTA: Todas as funções de desenho alteram o canvas, mas só aparecem ao chamar `atualizar()`.

---

# Transformar

### `transformar_deslocamento(forma, deslocamento: Vector2D)`

* Move a forma em `deslocamento`.

```python
ponto = canvas.criar_ponto(
    canvas.vec2d(0, 0),
    "@"
)
ponto = canvas.transformar_deslocamento(
    ponto,
    (1, 1)
)
# move `ponto` em 1 coluna e 1 linha
```

### `transformar_tamanho(forma, tamanho: Vector2D)`

* Aumenta a forma em `tamanho`

```python
ponto = canvas.criar_ponto(
    canvas.vec2d(0, 0),
    "@"
)
ponto = canvas.transformar_tamanho(
    ponto,
    (4, 4)
)
# aumenta o ponto
# (1, 1) -> (4, 4)
```