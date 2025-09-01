
def dividir(n1, n2):
    if n2 == 0:
        print("Divisão por zero não é permitida.")
    else:
        resultado = n1 / n2
        # print(f"{n1} / {n2} = {resultado}")
        return resultado

divisao = dividir(80, 0)
print("O resultado da divisão é", divisao)

print("Resultado", dividir(20, 4))

resultado = dividir(3, 5)
soma = 20 + resultado
print("A soma é", soma)

dividir(6, 3)