def sum_numbers(numbers):
    """
    Função para calcular a soma de uma lista de números.
    
    :param numbers: Lista de números (inteiros ou floats)
    :return: A soma dos números
    """
    if not numbers:
        return 0
    return sum(numbers)

def average_numbers(numbers):
    """
    Função para calcular a média de uma lista de números.
    
    :param numbers: Lista de números (inteiros ou floats)
    :return: A média dos números
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)