# PyTTB Atalhos

## Sumário

1. [Guia de Uso](#guia-de-uso)
2. [Funcionalidades Principais](#funcionalidades-principais)
    2.1. [adicionar_atalho](#adicionar_atalhotecla-str---str)
    2.2. [pegar_atalho](#pegar_atalhotecla-str---str)
    2.3. [remover_atalho](#remover_atalhotecla-str---none)
    2.4. [tecla_pressionada](#tecla_pressionadatecla-str-funcao-callable--none---callable--none)
    2.5. [desconectar_atalho](#desconectar_atalhotecla-str-funcao-callable---none)
    2.6. [chamar_atalho](#chamar_atalhotecla-str--args-kwargs---none)
    2.7. [tecla_solta](#tecla_soltatecla-str-funcao-callable--none---callable--none)
    2.8. [tecla_ativada](#tecla_ativadatecla-str-funcao-callable--none---callable--none)
    2.9. [verificar_atalhos](#verificar_atalhos---none)
    2.10. [esperar_por_tecla](#esperar_por_teclatecla-str---none)

---

## Guia de Uso

Importe o módulo:

```python
from PyTTB import atalhos
```

As funções permitem criar atalhos de teclado vinculados a eventos e funções personalizadas.

---

## Funcionalidades Principais

### `adicionar_atalho(tecla: str) -> str`

Cria e registra um novo atalho para uma tecla.

```python
atalhos.adicionar_atalho('q')
```

---

### `pegar_atalho(tecla: str) -> str`

Retorna o identificador do evento associado à tecla.

```python
evento_q = atalhos.pegar_atalho('q')
```

---

### `remover_atalho(tecla: str) -> None`

Remove um atalho e seu evento correspondente.

```python
atalhos.remover_atalho('q')
```

---

### `tecla_pressionada(tecla: str, funcao: Callable | None = None) -> Callable | None`

Conecta uma função ao evento da tecla pressionada. Pode ser usado como decorador.

```python
@atalhos.tecla_pressionada('q')
def sair():
    print("Saindo...")
```

ou

```python
atalhos.tecla_pressionada('q', sair)
```

---

### `desconectar_atalho(tecla: str, funcao: Callable) -> None`

Desconecta uma função do atalho especificado.

```python
atalhos.desconectar_atalho('q', sair)
```

---

### `chamar_atalho(tecla: str, *args, **kwargs) -> None`

Força a execução manual do evento da tecla.

```python
atalhos.chamar_atalho('q')
```

---

### `tecla_solta(tecla: str, funcao: Callable | None = None) -> Callable | None`

Executa a função quando a tecla é liberada.

```python
@atalhos.tecla_solta('w')
def liberou():
    print("W solta")
```

---

### `tecla_ativada(tecla: str, funcao: Callable | None = None) -> Callable | None`

Executa a função toda vez que a tecla é pressionada (ativa).

```python
@atalhos.tecla_ativada('a')
def apertou():
    print("A ativada")
```

---

### `verificar_atalhos() -> None`

Verifica o estado atual das teclas, disparando os eventos correspondentes.
Deve ser chamado dentro do loop principal do jogo/aplicação.

```python
while True:
    atalhos.verificar_atalhos()
```

---

### `esperar_por_tecla(tecla: str) -> None`

Bloqueia a execução até a tecla especificada ser pressionada.

```python
atalhos.esperar_por_tecla('e')
```

---

### Notas

* Depende do módulo `PyTTB.teclado` para capturar entradas.
* Recomendado chamar `verificar_atalhos()` em cada frame.
* Suporta múltiplos callbacks por tecla.
