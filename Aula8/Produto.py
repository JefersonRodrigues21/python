class Produto:

    def __init__(self, nome, valor, marca = '', modelo = ''):
        self.nome = nome
        self.valor = valor
        self.marca = marca
        self.modelo = modelo

produto0 = Produto('Celular', 1500, 'Samsung', 'Galaxy S21')

produto1 = Produto('Geladeira', 2500, 'Brastemp', 'BRM44')

produto2 = Produto('Notebook', 5000, 'Dell', 'Inspiron 15')


print(produto0.__dict__)
print(produto1.__dict__)
print(produto2.__dict__)