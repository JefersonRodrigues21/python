from sklearn.cluster import KMeans # Importa KMeans do sklearn
import numpy as np

class Produto:
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso

produtos = [
    Produto("Produto 1", 60.50, 0.70),
    Produto("Produto 2", 25, 0.5),
    Produto("Produto 3", 5.99, 0.28),
    Produto("Produto 4", 50, 0.78),
    Produto("Produto 5", 15.99, 0.38),
    Produto("Produto 6", 8.75, 0.15),
]

precos = [[p.preco, p.peso] for p in produtos] # Lista de listas com [preco, peso]
matriz = np.array(precos) # Converte para matriz numpy

kmeans = KMeans(n_init='auto', n_clusters=4, random_state=0).fit(matriz) # Aplica KMeans
labels = kmeans.labels_ # Obtém os rótulos dos clusters

for i in range(4): # Para cada grupo
    print(f"Grupo {i+1}:") # Itera sobre os grupos
    for j in range(len(produtos)): # Itera sobre os produtos
        if labels[j] == i: # Verifica se o produto pertence ao grupo i
            print(" - ", produtos[j].nome) # Imprime o nome do produto