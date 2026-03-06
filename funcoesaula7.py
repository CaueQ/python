notas = [7.5,8.0,9.5,6.0,8.5,]
print("notas: ", notas)

print("menor nota: ", min(notas))
print("maior nota: ", max(notas))
print("soma: ", sum(notas))
print("media: ", sum(notas) / len(notas))


nomes = ["adriana", "barbara", "carla", "daniel"]
print("usando FOR simples:")
for nome in nomes:
    print(f"ola, {nome}")

print("usando enumerate: ")

for indice, nome in enumarate(nomes):
    print(f"posição {indice}: {nome}")


original = ["A", "B", "C"]
copia = list(original)

print("original: ", original)
print("copia: ", copia)
print("sao iguais: ", original == copia)

copia.append("D")
print("original: ", original)
print("copia: ", copia)
print("sao iguais: ", original == copia)