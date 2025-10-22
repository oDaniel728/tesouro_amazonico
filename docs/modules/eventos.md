# PyTTB Eventos

_Imagine que você possui uma fabrica, cheio de trabalhadores.
Esses trabalhadores estão esperando pelo chamado do sino,
quando o sino tocar, os trabalhadores farão as suas funções._

Ao invés de trabalhadores, serão funções e ao invés de um sino, será uma função.

## Sumário
1. [Guia de uso](#guia-de-uso)
2. [Funcionalidades Principais](#funcionalidades-principais)  
2.1. [criar_evento](#criar_eventonome-str---evento)  
2.1. [remover_evento](#remover_eventonome-evento)  
2.1. [conectar_funcao](#conectar_funcaonome-evento-funcao-func---int)  
2.1. [desconectar_funcao](#desconectar_funcaonome-evento-funcao-func)  
2.1. [chamar_evento](#chamar_eventonome-evento)  
3. [Exemplos](#exemplos)

## Guia de uso
Primeiro Passo: Importe os eventos de PyTTB:
```py
from PyTTB import eventos
```
- Agora você já possui todas as funcionalidades dos eventos.
---
## Funcionalidades Principais
### `criar_evento(nome: str) -> evento`
- Cria um evento para ser utilizado, uma "fábrica".
```py
evento = criar_evento("evento")
#^^^^^                 ^^^^^^
# o nome dentro de criar_evento deve
# ser igual ao nome da variável
# (recomendo)
```
- Retorna o evento
> NOTA: É opcional guardar numa variável, ela é apenas o **endereço** do evento.
### `remover_evento(nome: evento)`
- Deleta o evento `nome`
```py
remover_evento(evento)
# `evento` deve existir.
# `evento` deve ter sido criado anteriormente.
```

### `conectar_funcao(nome: evento, funcao: func) -> int`
- Conecta uma função ao evento, fazendo ela esperar pelo chamado
```py
def _quando_evento_for_chamado():
    print("Chamado")
conectar_funcao(evento, _quando_evento_for_chamado)
```

### `conectar_uma_vez(nome: evento, funcao: func) -> int`
- Conecta uma função ao evento, mas ela só pode ser chamada uma vez, depois disso ela some.
```py
def _quando_evento_for_chamado_unico():
    print("Chamado unico")
conectar_funcao(evento, _quando_evento_for_chamado_unico)
```

### `desconectar_funcao(nome: evento, funcao: func)`
- Desconecta uma função ao evento, demitindo ela.
```py
desconectar_funcao(evento, _quando_evento_for_chamado_unico)
```

### `chamar_evento(nome: evento, *)`
- Chama todas as funções conectadas ao evento `nome`.
```py
chamar_evento(evento)
# chama _quando_evento_for_chamado,
# _quando_evento_for_chamado_unico foi desconectado anteriormente.

# * se trata dos argumentos das funções
```

## Exemplos
- Aqui estão exemplos de uso para os eventos.

### 1. Para detectar teclas
```py
from PyTTB import eventos, teclado, terminal

rodando = True
tecla_pressionada = eventos.criar_evento("tecla_pressionada")

def _quando_tecla_pressionada(tecla: str):
    terminal.escreval(f"Tecla pressionada: {tecla}")
    terminal.atualizar()

    global rodando
    # permite que rodando possa ser trocado dentro dessa função
    if tecla == 'q':
        rodando = False

while rodando:
    tecla = teclado.tecla_pressionada()
    if tecla:
        eventos.chamar_evento(tecla_pressionada, (tecla))

# roda o programa até apertar 'q'
```

### 2. Para detectar frames
- Vamos reutilizar o exemplo passado
```py
from PyTTB import eventos, teclado, terminal

rodando = True
tecla_pressionada = eventos.criar_evento("tecla_pressionada")

def _quando_tecla_pressionada(tecla: str):
    terminal.escreval(f"Tecla pressionada: {tecla}")
    terminal.atualizar()

    global rodando
    # permite que rodando possa ser trocado dentro dessa função
    if tecla == 'q':
        rodando = False

## TRECHO NOVO

frame_carregado = eventos.criar_evento("frame_carregado")

def _quando_frame_carregado():
    ...

desenhar_frame = eventos.criar_evento("desenhar_frame")
def _quando_desenhar_frame():
    ...

## TRECHO ANTIGO

while rodando:
    ## TRECHO NOVO
    evento.chamar_evento(frame_carregado)
    ## TRECHO ANTIGO
    tecla = teclado.tecla_pressionada()
    
    if tecla:
        eventos.chamar_evento(tecla_pressionada, (tecla))
    
    ## TRECHO NOVO
    evento.chamar_evento(desenhar_frame)
    ## TRECHO ANTIGO
# roda o programa até apertar 'q'
```