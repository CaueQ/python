Pães = int(input("quantos pães você vendeu essa semana?"))
Doces = int(input("quantos doces você vendeu essa semana?"))
Bolos = int(input("quantos bolos você vendeu essa semana?"))

total = (Pães * 1) + (Doces * 2) + (Bolos * 3)

if total > 150:
    print("você ganhou um bolo")
    elif total >= 100:
    print("você ganhou um doce")
    else total < 100:
    print("Ganhou um pão")