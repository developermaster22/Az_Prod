def siguiente_estado(estado_actual):
    flujo = ['diseñador', 'impresor', 'entelador', 'embolsador', 'finalizado']
    try:
        indice = flujo.index(estado_actual)
        if indice < len(flujo) - 1:
            return flujo[indice + 1]
        else:
            return estado_actual  # ya está finalizado
    except ValueError:
        return estado_actual

def estado_anterior(estado_actual):
    flujo = ['diseñador', 'impresor', 'entelador', 'embolsador', 'finalizado']
    try:
        indice = flujo.index(estado_actual)
        if indice > 0:
            return flujo[indice - 1]
        else:
            return estado_actual  # no puede retroceder más
    except ValueError:
        return estado_actual
