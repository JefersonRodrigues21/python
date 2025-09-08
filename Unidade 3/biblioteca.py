import math # importa a biblioteca matemática
import random # importa a biblioteca de números aleatórios

nota = 6.4
# print(round(nota)) # arredonda para o inteiro mais próximo
# print(round(nota, 2)) # arredonda para 2 casas decimais
# print(math.ceil(nota)) # arredonda para cima
# print(math.floor(nota)) # arredonda para baixo
# print(math.sqrt(25)) # raiz quadrada

print(round(random.random() * 100)) # número aleatório entre 0 e 100
print(round(random.uniform(50, 100))) # número aleatório entre 50 e

print(random.randint(1, 10)) # número inteiro aleatório entre 1 e 10 10
print(random.choice(['Maria', 'João', 'Ana', 'Pedro'])) # escolhe um elemento aleatório de uma lista    
print(random.sample(range(1, 100), 5)) # escolhe 5 números aleatórios entre 1 e 100
print(random.shuffle([1, 2, 3, 4, 5])) # embaralha a lista
print(random.shuffle(['Maria', 'João', 'Ana', 'Pedro'])) # embaralha a lista
print(random.shuffle('abcdefg')) # embaralha a string
print(random.choices(['Maria', 'João', 'Ana', 'Pedro'], k=2)) # escolhe 2 elementos aleatórios de uma lista, com reposição
print(random.choices(range(1, 100), k=5)) # escolhe 5 números aleatórios entre 1 e 100, com reposição