from datetime import datetime # Importa a classe datetime do módulo datetime

def formatarData(data = datetime.now(), formato = '%d/%m/%Y'): # Define a data padrão como a data e hora atuais
    return datetime.strftime(data, formato) # Formata a data no padrão brasileiro

def criarData(data, formato = '%Y/%m/%d'): # Função para criar um objeto datetime a partir de uma string
    return datetime.strptime(data, formato) # Converte a string em um objeto datetime usando o formato especificado

# print(formatarData()) # Exibe a data atual formatada no padrão brasileiro
# print(criarData('2023/06/25')) # Cria um objeto datetime a partir da string