numeros = [10, 20, 30, 17, 58, 3, 7]
#print(numeros[5])  # Acessa o elemento no índice 5 (sexto elemento)

carros = ['Pálio', 'Gol', 'Virtus', 'Ka', 'Onix', 'Celta', 'Ferrari', 'Tcross']
#print(carros[2])
#print(len(carros))  # Retorna o tamanho da lista
print('1 ->', carros)

carros.append('Kombi') # Adiciona um elemento ao final da lista
print('2 ->', carros)

carros.remove('Gol') # Remove um elemento da lista
print('3 ->', carros)

del carros[3] # Remove o elemento no índice 3 (quarto elemento)
print('4 ->', carros)

carros = sorted(carros) # Ordena a lista em ordem alfabética
print('5 ->', carros)

for carro in carros:
    print(carro)