""" Algoritmo para calcular o estoque médio de uma peça """
quantidade_min = int(input('Quantidade minima: '))
quantidade_max = int(input('Quantidade maxima: '))

estoque_medio = (quantidade_min + quantidade_max) / 2

print('A média do estoque é:', int(estoque_medio))
