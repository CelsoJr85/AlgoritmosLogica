""" Com dados sobre altura e sexo de uma pessoa, retornar seu peso ideal """
altura = float(input('Qual a sua altura? '))
sexo = input('Qual o seu sexo? (M/F) ')

if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
    print('Sexo não reconhecido.')

print(f'Seu peso ideal é: {peso_ideal:.2f}kg')
