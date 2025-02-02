""" João comprou um computador para lhe ajudar em seu trabalho. Todas às vezes que pesar um peixe maior que o
    estabelecido pela lei, 50 kilos, tem que pagar uma multa de R$ 4,00 por quilo excedente. Algoritmo para ler
    o peso do peixe, e verificar set há excedente de peso. Se houver gravar uma variavel com o tanto de peso a
    mais que o estabelecido, e em outra variavel o valor do peso excedente. ao contrario mostra na variavel o valor 0"""
e = 0
n = 0
peso = float(input('Digite o peso do peixe: '))

if peso > 50:
    e = peso - 50
    n = e * 4

print(f'Peso do peixe: {peso} kg. \nPeso excedente: {e} Kg. \nValor da multa: R$ {n:.2f}')
