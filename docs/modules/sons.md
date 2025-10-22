# PyTTB Audio

## Sumário
1. [Guia de uso](#guia-de-uso)
2. [Funcionalidades Principais](#funcionalidades-principais)  
2.1. [tocar_audio](#tocar_audiocaminho-str---audio)  
2.2. [parar_audio](#parar_audioprocesso-audio)  


## Guia de uso
Primeiro Passo: Importe o audio de PyTTB:
```py
from PyTTB import audio
```
- Agora você já possui todas as funcionalidades dos sons.
---
## Funcionalidades Principais
### `tocar_audio(caminho: str) -> audio`
- Toca o audio no `caminho` somente se for um `.wav`.
```python
som = audio.tocar_audio("audio.wav")
```

### `parar_audio(processo: audio)`
- Para de tocar o audio do `processo`.
```python
# TRECHO ANTIGO

som = audio.tocar_audio("audio.wav")

# TRECHO NOVO

audio.parar_audio(som)

```