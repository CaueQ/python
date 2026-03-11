contato = {
    "@camila": "Camila",
    "@paola": "Paola",
    "@sheron": "Sheron",
    "@bruna": "Bruna",
    "@joao": "joao"
}

# Obter chaves
print("chaves: ")
for insta in contato.key():
    print(insta)

#Obter valores
print("\n Valores:")
for nome in contato.values():
    print(nome)

#Obter pares (chave-valor)
print("\n pares: ")
for insta, nome in contato.items():
    print(f"{insta} --> {nome}")

contato = {
    "@camila": 1.66,
    "@paola": 1.50,
    "@sheron": 1.80,
    "@bruna": 1.60,
    "@joao": 1.70
}

#ordenar por chave
print("ordenar por chaves: ")
for insta in sorted(contato.key()):
    print(f"{insta} --> {contato[insta]:.2f}m")

#ordenar por valor
from operator import itemgetter
print("\n ordenado por valor (altura): ")
for insta, estatura in sorted(contato.items(), key=itemgetter(1)):
    print(f"{insta} --> {estatura:.2f}m")