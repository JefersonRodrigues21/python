def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return("Divisão por zero não é permitida.")
    else:
        resultado = n1 / n2
        # print(f"{n1} / {n2} = {resultado}")
        return resultado

def calcular(n1, n2, operador):
    match operador:
        case '+': return add(n1, n2)
        case '-': return subtract(n1, n2)
        case '*': return multiply(n1, n2)
        case '/': return divide(n1, n2)
        case other: return "Operador inválido"

print(calcular(5, 10, '+'))
print(calcular(5, 10, '-'))
print(calcular(5, 10, '*'))
print(calcular(5, 0, '/'))
print(calcular(5, 10, 'o'))

'''
divisao = dividir(80, 0)
print("O resultado da divisão é", divisao)

print("Resultado", dividir(20, 4))

resultado = dividir(3, 1)
soma = 20 + resultado
print("A soma é", soma)

dividir(6, 0)
'''