""" Algoritmo para calcular horas trabalhadas. Onde um trabalhador que recebe 10,00 a hora, trabalha 50 horas.
    Assim, ele trabalhando mais que 50 horas, recebe 20,00 por hora extra. Imprimir salario e valores extras."""
valor_da_hora = 10
valor_extra = 20

e = 0
n = float(input('Digite quantidade de horas trabalhadas: '))
l = (valor_da_hora * 50) - e

if n > 50:
    e = (n - 50) * valor_extra
    salario = (50 * valor_da_hora) + e
    print(f'Salário bruto: R$ {salario:.2f}')
    print(f'Salario extra: R$ {e:.2f}')
    print(f'Salario liquido: R$ {l:.2f}')

else:
    salario = (n * valor_da_hora)
    print(f'Salário bruto: R$ {salario:.2f}')
    print(f'Salario extra: R$ {e:.2f}')
    print(f'Salario liquido: R$ {l:.2f}')
