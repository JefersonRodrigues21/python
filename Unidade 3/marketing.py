import matplotlib.pyplot as plt # biblioteca para visualização de dados
# Para instalar a biblioteca, use: pip install matplotlib
class Campanha:
    def __init__(self, canal, investimento, cliques, conversoes):
        self.canal = canal
        self.investimento = investimento
        self.cliques = cliques
        self.conversoes = conversoes

    def cpc(self): # Custo por Clique
        return self.investimento / self.cliques

campanhas = [
    Campanha("Facebook Ads", 1000, 15000, 150),
    Campanha("Google Ads", 1200, 10000, 200),
    Campanha("Email Ads", 5000, 5000, 50),
    Campanha("Instagram Ads", 800, 12000, 80),
]

canais = [c.canal for c in campanhas] # Lista de canais
cpcs = [c.cpc() for c in campanhas] # Lista de CPCs

plt.bar(canais, cpcs)
plt.title("Custo por Clique")
plt.xlabel("Canais")
plt.ylabel("Custo em (R$)")
plt.show()