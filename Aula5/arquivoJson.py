import json

pessoas = [ # Lista de pessoas
    {"nome": "Joao", "telefone": '(65) 97777-7777', 'endereco': 'Rua A, 123'},
    {"nome": "Maria", "telefone": '(65) 98888-8888', 'endereco': 'Rua B, 456'},
    {"nome": "Jose", "telefone": '(65) 99999-9999', 'endereco': 'Rua C, 789'}
]

with open('pessoas.json', 'w') as arquivo: # Abre o arquivo em modo de escrita
    json.dump(pessoas, arquivo, indent=4) # Escreve a lista de pessoas no arquivo em formato JSON