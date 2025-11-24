_timeline = list
_timestamp = float

def criar(duracao: float) -> _timeline:
    return[duracao, 0]

def __pegar_timestamp(tm: _timeline, ts: _timestamp | float) -> float:
    duracao = float(tm[0]) # duração em segundos
    return(ts % duracao)

def timestamp(timeline: _timeline, timestamp: float) -> float:
    r = __pegar_timestamp(timeline, timestamp)
    timeline[1] = r
    return(r)

def pegar_timestamp(timeline: _timeline) -> float:
    return(timeline[1])
def pegar_duracao(timeline: _timeline) -> float:
    return(timeline[0])

def relativo(timeline: _timeline) -> float: # (...) -> [0, 1]:
    return(pegar_timestamp(timeline) / pegar_duracao(timeline))

def porcentagem(timeline: _timeline) -> float: # (...) -> [0, 100]:
    return(relativo(timeline) * 100)

def passou_de(timeline: _timeline, duracao: float) -> bool:
    return(pegar_timestamp(timeline) > duracao)

def tempo_entre(timeline: _timeline, a: float, b: float) -> bool: # x (pertencente) [a, b]:
    return(a <= pegar_timestamp(timeline) <= b) 

def resetar(timeline: _timeline) -> None:
    timeline[1] = 0

def progredir(timeline: _timeline, delta: float) -> None:
    timeline[1] += delta
    if passou_de(timeline, pegar_duracao(timeline)):
        resetar(timeline)