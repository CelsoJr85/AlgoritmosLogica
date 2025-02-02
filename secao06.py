""" Verificar se número é par ou impar e armazenar. """
p = 0
i = 0

valor = int(input('Digite um valor: '))
if valor % 2 == 0:
    p = valor
else:
    i = valor

print(f'Par: {p} \nImpar: {i}')
