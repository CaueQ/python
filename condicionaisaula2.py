nome = input("digite seu nome: ")
if len(nome) > 50:
    print("seu nome é grande, ele pode possuir mais de 20 letras ")
print(f"ele possui {len(nome)} caracteres.")


valor = int(input("digite um numero: "))
if valor % 2 == 0:
    print("o numero é par")
else:
    print("o numero é impar")

nota = float(input("digite sua nota"))

if nota > 10:
    print("passou")
else:
    if nota == 7:
        print("pode melhorar")
    else:
        print("reculperacao")
    
    else:
        print("reculperacao")
    
    idade = int(input("digite a idade: "))

    if idade >= 16 and idade <= 69:
        print("faixa permitida")
    else:
        print("fora da faixa")