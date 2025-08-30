'''
try:
    # Código que pode gerar uma exceção
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    
    resultado = n1 / n2
    
    print(f"O Resultado da divisão é {resultado}")
    
except Exception as erro:
    print(f"Ocorreu um erro: {erro}")
'''
try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
        
    resultado = n1 / n2
        
    print(f"O Resultado da divisão é {resultado}")

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite números inteiros.")

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

except Exception as erro:
    print(f"Ocorreu um erro: {erro}")

else:
    print("Operação concluída com sucesso.")

finally:
    print("Fim da operação")