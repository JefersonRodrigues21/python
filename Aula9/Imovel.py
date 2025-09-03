class Imovel:
    def __init__(self, nome, uf, valor, endereco='', area=''): # <--- Adicionando parâmetros
        self.nome = nome
        self.uf = uf
        self.valor = valor
        self.endereco = endereco
        self.area = area
    
    def detalhar(self):
        print(self.__dict__)
    
    def calcularImposto(self):
        return self.valor * 0.02

class ImovelResidencial(Imovel): # <--- Herdando de Imovel
    def __init__(self, nome, uf, valor, endereco='', area=''):
        super().__init__(nome, uf, valor, endereco, area='') # <--- Chamando o construtor da classe pai
        self.quartos = 0
        self.piscina = False

class ImovelComercial(Imovel):
    ...

casa = ImovelResidencial('Minha Casa', 'SP', 300000)
casa.detalhar()

clinica = ImovelComercial('Clinica x', 'SP', 800000)
clinica.detalhar()
'''
imovel = Imovel('Solar do Cerrado', 'DF', 500000)
imovel.endereco = 'ABC'
imovel.area = '2000'
imovel.detalhar()
'''