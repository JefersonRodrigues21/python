from abc import ABC, abstractmethod

class Imovel(ABC):
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

    @abstractmethod
    def aluguelSugerido(self):
        ...

class ImovelResidencial(Imovel): # <--- Herdando de Imovel
    def __init__(self, nome, uf, valor, endereco='', area=''):
        super().__init__(nome, uf, valor, endereco, area='') # <--- Chamando o construtor da classe pai
        self.quartos = 0
        self.piscina = False
    
    def aluguelSugerido(self):
        return self.valor * 0.01

class ImovelComercial(Imovel):
    
    def aluguelSugerido(self):
        return self.valor * 0.015

class ImovelRural():
    def __init__(self, hectares = '', curral = '', produtiva = True):
        self.hectares = hectares
        self.curral = curral
        self.produtiva = produtiva
    
    def mesPlantacao(self, mes):
        match int(mes):
            case 1: print('Milho')
            case 2: print('Feijão')
            case 3: print('Soja')
            case other: print('Algodão')

class Fazenda(Imovel, ImovelRural):

    def aluguelSugerido(self):
        return self.valor * 0.025



'''
fazenda = Fazenda('Fazenda Modelo', 'GO', 1500000)
fazenda.detalhar()
print(fazenda.calcularImposto())
fazenda.mesPlantacao(2)
'''


casa = ImovelResidencial('Minha Casa', 'SP', 300000)
casa.detalhar()
print(casa.aluguelSugerido())

clinica = ImovelComercial('Clinica x', 'SP', 800000)
clinica.detalhar()



'''
imovel = Imovel('Solar do Cerrado', 'DF', 500000)
imovel.detalhar()
imovel.endereco = 'ABC'
imovel.area = '2000'
'''