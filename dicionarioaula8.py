matricula1 = 2026001
nome1 = "Ana Silva"
telefone1 = "9999-8888"

aluno = {
    "matricula": 2026001
    "nome": "Ana Silva"
    "telefone": "9999-8888"
}

print(aluno)

contato = {
    "@camila": "Camila",
    "@paola": "Paola",
    "@sheron": "Sheron",
    "@bruna": "Bruna",
    "@joao": "joao"
}

print(contato)
print(type(contato))

print(contato["@camila"])


print(contato.get("@paola"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "não encontrado"))

print("Original: ", contato)

contato["@giovana"] = "Giovana"
print("Apos add: ", contato)

contato["@paola"] = "Paola Oliveira"
print("Apos add: ", contato)

contato.update(
    {
        "@bruna": "Bruna Marquezine",
        "@camila": "Camila Q."
    }
)

print("Apos atualização: ", contato)

removido = contato.pop("@sheron")
print(f"removido: {removido}")
print("Apos o pop: ", contato)

del contato["@paola"]
print("Apos o del: ", contato)

copia = dict(contato)
contato.clear()
print("Apos clear: ", contato)
print("copia: ", copia)

print("numero de contato: ", len(contato))

contato.pop("@camila")
print("Apos remover um: ", len(contato))

if "@joao" in contato:
    print(f"Encontrado: {contato}")

if "@inexistente" in contato:
    print("Existe")
else:
    print("não existe.")

vazio = {}

dados = {
    "nome": "joão",
    "idade": 25,
    "altura": 1.70,
    "ativo": True
}

print("vazio: ", vazio)
print("vazio: ", dados)