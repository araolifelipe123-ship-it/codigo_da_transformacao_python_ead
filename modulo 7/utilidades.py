def calcular_media(lista_numeros):
    
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)


def e_par(numero):
    return numero % 2 == 0

def soma(a, b):
    
    return a + b


def subtrair(a, b):
    
    return a - b


def multiplicar(a,b):
    
    return a * b

def multiplicar(a,b):
    
    return a * b


def dividir(a,b):
    
    if b == 0:
        return "erro: divisao por zero nao permitida"
    return a / b


def divisao_inteira(a, b):
    """
    retorna apenas a parte inteira da divisao de 'a' por 'b'.
    parametros: a (int/float)
    retorno: o quociente inteiro ou uma mensagem de erro se b == 0.
    """
    if b == 0:
        return "erro: divisao por zero nao e permitida."
    return a // b

def resto_divisao(a, b):
    """
    
    calcula o resto da divisao (modulo) de 'a' por 'b'.
    parametros: a (int/float), b (int/float)
    retorno: o resto da dvisao ou uma mensagem de erro se b == 0.
    """
    if b == 0:
        return "erro: divisao por zero nao e permitida."
    return a % b

def potencia(base, expoente):
    """
    
    eleva a base ao expoente (potenciacao).
    parametros: base (int/float), expoente (int/float)
    retorno: o resultado de base elevado ao expoente.
    """
    
    return base ** expoente


def calcular_media(lista_numeros):
    
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)