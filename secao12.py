""" Tabuada de qualquer número entre 1 e 1 milhão """

numero = int(input("Digite um número: "))

for i in range(1, 11):
    valor = numero * i
    print(f"{numero} x {i} = {numero * i}")
