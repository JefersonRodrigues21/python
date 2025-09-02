numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 33, 44, 55, 66, 77]

resultado = filter(lambda n: n % 2 == 1, numeros)
print(list(resultado)) 
# Exemplo de números ímpares: 1, 3, 5, 7, 9, 33, 55, 77