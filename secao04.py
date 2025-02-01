""" Algoritmo para calcular salário / com cores nos valores de saída """
horas_trabalhadas = float(input('Quantas horas trabalhadas? '))
valor_da_hora = float(input('Qual o valor da hora? '))

multiplicador = horas_trabalhadas * valor_da_hora

print(f"Você trabalhou \033[34m{horas_trabalhadas:.0f} \033[0mhoras, e neste mês irá receber \033[32mR${multiplicador:.2f}")
