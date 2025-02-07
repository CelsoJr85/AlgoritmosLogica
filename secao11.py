""" Algoritmo para separar nível de nadadores de acordo com idade. Infantil-a de 5 a 7 anos. Infantil-b de 8 a 11 anos.
    Juvenil-a de 12 a 13 anos. Juvenil-b de 14 a 17 anos. Adulto de 18 anos ou mais. """

idade = int(input("Digite sua idade: "))
if idade <= 7:
    print("Infantil-a")
elif idade <= 11:
    print("Infantil-b")
elif idade <= 13:
    print("Juvenil-a")
elif idade <= 17:
    print("Juvenil-b")
else:
    print("Adulto")
