# Guia de uso
PyTTB(ou Python Terminal ToolBox) é uma caixa de ferramentas feita com o objetivo de fornecer ferramentas para interação com o terminal sem uma abordagem orientada à objetos.

## 1 Passo: Importação
Importe usando o `import`
```py
import PyTTB
```
---
> Ela possui 2 módulos principais.
- ✍ [Terminal](modules/terminal.md): _Manipulação do terminal._
- 🎨 [Canvas](modules/canvas.md): _Desenhos no terminal._
- 🎮 [Teclado](modules/teclado.md): _Absorção de teclas pelo terminal._
- 🔔 [Eventos](modules/eventos.md): _Criação de eventos._

### Terminal
Manipulação, leitura e escrita do terminal, e algumas funções extras como `.aguarde(float)`;  
Formatações com cores e estilos de texto.

### Canvas
Utiliza o [PyTTB.Terminal](#terminal) para escrever e manipular o terminal com algumas adições, tendo o principal foco em ter a possibilidade de desenhar no terminal, utilizando caracteres como _"pinceis"_.