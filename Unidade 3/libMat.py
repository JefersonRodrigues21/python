import matplotlib.pyplot as plt # importa a biblioteca matplotlib

'''
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
qtdTi = [60, 52, 76, 89, 108, 95]
qtdRh = [40, 72, 17, 28, 87, 56]

# plt.bar(meses, valores) # cria o gráfico de barras
plt.plot(meses, qtdTi, label='TI', color = 'red', marker = '.') # cria o gráfico de linha para TI
plt.plot(meses, qtdRh, label='RH', color = 'blue', marker = '.') # cria o gráfico de linha para RH
plt.title('Chamados abertos') # adiciona o título ao gráfico
plt.xlabel('Meses') # adiciona o rótulo do eixo x
plt.ylabel('Quantidade') # adiciona o rótulo do eixo y
plt.legend() # adiciona a legenda ao gráfico
plt.show()
'''
navegadores = ['Chrome', 'Edge', 'Firefox']
qtd = [1200, 600, 200]
cores = ['blue', 'green', 'red']

plt.pie(qtd, labels=navegadores, colors=cores) # cria o gráfico de pizza
plt.show() # exibe o gráfico