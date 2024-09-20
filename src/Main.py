def soma_numeros(numeros):
    if not numeros:
        return 0
    return sum(numeros)

def media_numeros(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def produto_numeros(numeros):
    if not numeros:
        return 1
    produto = 1
    for num in numeros:
        produto *= num
    return produto

def diferenca_numeros(numeros):
    if not numeros:
        return 0
    return numeros[0] - sum(numeros[1:])

def numero_maximo(numeros):
    if not numeros:
        return None
    return max(numeros)

def numero_minimo(numeros):
    if not numeros:
        return None
    return min(numeros)