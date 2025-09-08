import pandas as pd # importa a biblioteca pandas para manipulação de dados

cidades = [
    {'nome': 'Distrito Federal', 'uf': 'DF', 'populacao': 3055149},
    {'nome': 'São Paulo', 'uf': 'SP', 'populacao': 12325232},
    {'nome': 'Rio de Janeiro', 'uf': 'RJ', 'populacao': 6747815},
    {'nome': 'Recife', 'uf': 'PE', 'populacao': 1645727},
]

dataFrame = pd.DataFrame(cidades) # cria um DataFrame a partir da lista de dicionários 100

ordenada = dataFrame.sort_values(by='populacao', ascending=False) # ordena o DataFrame pela coluna 'populacao' em ordem decrescente

print(ordenada) # exibe o DataFrame ordenado
print()
print(ordenada.head(2)['nome'])
