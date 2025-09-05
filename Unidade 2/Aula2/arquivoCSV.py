import csv

carros = [ # Lista de carros
    ['VW', 'Virtus', '2017'],
    ['HONDA', 'Civic', '2020'],
    ['CHEVROLET', 'Onix', '2018']
]

with open('carros.csv', 'w', newline='') as arquivo:
    fileCSV = csv.writer(arquivo, delimiter=";") # Define o delimitador como ponto e vírgula

    fileCSV.writerow(['Marca', 'Modelo', 'Ano']) # Escreve o cabeçalho
    fileCSV.writerows(carros) # Escreve os dados dos carros
