import tensorflow as tf # importa a biblioteca TensorFlow
# Instalação do TensorFlow - pip install tensorflow
class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

produtos = [
    Produto('Camiseta', 29.99, 'Roupas'),
    Produto('Calça', 79.99, 'Roupas'),
    Produto('Tênis', 99.99, 'Calçados'),
    Produto('Celular', 1499.99, 'Eletrônico'),
    Produto('Notebook', 3499.99, 'Eletrônico'),
    Produto('Livro', 19.99, 'Livros'),
]

nomes = tf.constant([p.nome for p in produtos])
precos = tf.constant([p.preco for p in produtos])
categorias = tf.constant([p.categoria for p in produtos])

media = tf.reduce_mean(precos)
eletronicos = tf.boolean_mask(nomes, tf.equal(categorias, 'Eletrônico'))

print(media)
print(eletronicos)