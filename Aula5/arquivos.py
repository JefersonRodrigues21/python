arquivo = open('pessoas.txt', 'r') # 'r' = read (leitura), 'w' = write (escrita), 'a' = append (adicionar) 
# Abre o arquivo para escrita # Abre o arquivo para leitura e escrita, criando-o se não existir
arquivo.write('João\n')
arquivo.write('Maria\n')
arquivo.write('José\n')

arquivo.close()

with open('pessoas.txt', 'r+') as arquivoLeitura:
    for linha in arquivoLeitura:
        print(linha)
        