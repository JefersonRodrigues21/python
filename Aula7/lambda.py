# Lambda - função anônima
numeros = [4, 8, 9, 3]
'''
resultado = []
for n in numeros:
    resultado.append(n * 2) # Multiplica cada elemento por 2 (append = adiciona um elemento ao final da lista)

print(numeros, resultado)

def multiplicar(n1):
    return n1 * 2
'''

resultado = map(lambda n: n * 3, numeros) # map = aplica uma função a cada elemento de uma lista    
print(numeros, list(resultado))