import numpy as np # importa a biblioteca numpy para cálculos numéricos

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0

for n in numeros:
    soma +=n

media = soma/ len(numeros) # calcula a média
print('Média na mão:', media)

array_numeros = np.array(numeros) # cria um array numpy

media = np.mean(array_numeros) # calcula a média usando numpy
print('Média com numpy:', media)