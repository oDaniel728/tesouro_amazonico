from . import dicionario

_buffer = list[list[str]]
_dicionario = dicionario._dicionario
_grafico = dicionario._dicionario
_posicao = list[int]

def criar(linhas: int, colunas: int) -> _buffer:
    return [[" "] * colunas for _ in range(linhas)]

def adicionar_ponto(buffer: _buffer, posicao: list[int], ponto: str) -> None:
    buffer[posicao[0]][posicao[1]] = ponto

def adicionar_dicionario(buffer: _buffer, dicionario: _dicionario) -> None:
    for pos, char in dicionario:
        adicionar_ponto(buffer, pos, char)

def empacotar(buffer: _buffer, grafico: _grafico, deslocamento: _posicao = [0, 0]) -> None:
    for pos, char in grafico:
        adicionar_ponto(
            buffer, 
            [
                pos[1] + deslocamento[1], 
                pos[0] + deslocamento[0]
            ], 
            char
        )

def pegar_ponto(buffer: _buffer, posicao: list[int]) -> str:
    return buffer[posicao[0]][posicao[1]]

def pegar_dicionario(buffer: _buffer, ignorar: list[str] = [' ']) -> _dicionario:
    d = dicionario.criar()

    for i in range(len(buffer)):
        for j in range(len(buffer[i])):
            if pegar_ponto(buffer, [i, j]) not in ignorar:
                dicionario.adicionar(d, [i, j], buffer[i][j])

    return d

def limpar(buffer: _buffer) -> None:
    for i in range(len(buffer)):
        for j in range(len(buffer[i])):
            buffer[i][j] = " "

def para_string(buffer: _buffer) -> str:
    string = ""
    for linha in buffer:
        string += "".join(linha) + "\n"
    return string   