# Guia de uso
PyTTB(ou Python Terminal ToolBox) é uma caixa de ferramentas feita com o objetivo de fornecer ferramentas para interação com o terminal sem uma abordagem orientada à objetos.

## 1 Passo: Importação
Importe usando o `import`
```py
import PyTTB
```
---
> Ela possui 6 módulos principais.
- ✍ [Terminal](modules/terminal.md): _Manipulação do terminal._
- 🎨 [Canvas](modules/canvas.md): _Desenhos no terminal._
- 🎮 [Teclado](modules/teclado.md): _Absorção de teclas pelo terminal._
- 🔔 [Eventos](modules/eventos.md): _Criação de eventos._
- ⏫ [Atalhos](modules/atalhos.md): _Criação de atalhos._
- 🎧 [Audio](modules/sons.md): _Tocagem de áudios no terminal._

### Terminal
Manipulação, leitura e escrita do terminal, e algumas funções extras como `.aguarde(float)`;  
Formatações com cores e estilos de texto.

### Canvas
Utiliza o [PyTTB.Terminal](#terminal) para escrever e manipular o terminal com algumas adições, tendo o principal foco em ter a possibilidade de desenhar no terminal, utilizando caracteres como _"pinceis"_.

### Teclado
Detecta teclas de teclado.

### Eventos
Criação, conexão e desconexão de eventos.

### Atalhos
Sistema de atalhos de teclado utilizando [PyTTB.teclado](#teclado).

### Audio
Tocagem de áudios no terminal.