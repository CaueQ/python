pontos = int(input("quantos pontos c tem: "))
derrotas = int(input("quantas derrotas c tem: "))

total = pontos - (derrotas * 10)

if total <= 100:
    print("bronze")
elif total <= 300:
    print("prata")
elif total <= 600:
    print("ouro")
elif total >= 600:
    print("dima")