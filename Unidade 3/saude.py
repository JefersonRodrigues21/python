import numpy as np 
import pandas as pd # Para instalar a biblioteca, use: pip install pandas

class Paciente:
    def __init__(self, nome, idade, sexo, peso, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

pacientes = {
    'Paciente 1': Paciente('Maria', 25, 'F', 60, 1.70),
    'Paciente 2': Paciente('Orion', 30, 'M', 80, 1.80),
    'Paciente 3': Paciente('João', 45, 'M', 70, 1.85),
    'Paciente 4': Paciente('Ana', 35, 'F', 90, 1.65),
}

l_pacientes = [p.__dict__ for p in pacientes.values()] # cria lista de dicionários a partir dos atributos dos objetos

df_pacientes = pd.DataFrame.from_records(l_pacientes, index=pacientes.keys()) # cria dataframe a partir de lista de dicionários

df_pacientes['IMC'] = df_pacientes.apply(lambda i: i.peso / i.altura ** 2, axis=1) # calcula IMC e adiciona como nova coluna no dataframe

media = np.mean(df_pacientes['IMC']) # calcula média do IMC

sobrepeso = df_pacientes[df_pacientes['IMC'] > 25] # filtra pacientes com IMC maior que 25

percentual = len(sobrepeso) / len(df_pacientes) * 100 # calcula percentual de pacientes com sobrepeso

print(percentual)

