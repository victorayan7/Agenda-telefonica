#Declaração
nome_completo = "Victor Ferreira"

nome_completo_aspas = """Victor
Ferreira"""

nome_completo_quebra = "Victor \
Ferreira"

nome = "Victor"
sobrenome = "Ferreira"

#Formatação
print("Nome Completo (1a forma):" , nome_completo)
print("Nome Completo (2a forma):" + nome_completo)
print("Nome Completo (3a forma):" + "Victor" + "Ferreira")
print("Nome Completo (4a forma):" + "Victor", "Ferreira")
print("Nome Completo (5a forma):", nome_completo_aspas)
print("Nome Completo (6a forma):", nome_completo_quebra)
print("Nome Completo (7a forma): %s" % nome_completo)
print("Nome Completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome Completo (9a forma): {nome} {sobrenome}")
print("Nome Completo (10a forma): {} {}".format(sobrenome, nome))

#Maiuscula
print("nome: ", nome_completo.upper())

#Minuscula
print("nome: ", nome_completo.lower())

#Letra []
print("nome: ", nome_completo[0])

#Contar quantas ocorrencias tem na variavel
nome_completo.count("a")
print("", nome_completo.count("e"))

#Encontrar a posição da letra na variavel
nome_completo.find("a")
print("", nome_completo.find("a"))

#Codificar string em byte
nome_completo.encode()
print("", nome_completo.encode())

#Decodificar string em byte
nome_completo.encode().decode()
print("", nome_completo.encode().decode())

#Substituir indice por outro
nome_completo.replace("r", "s")
print("", nome_completo.replace("r", "s"))
print("", nome_completo.replace("r", "s").replace("e", "i"))

#separar por traço
print("-".join(nome_completo))

#dividir por lista
print(nome_completo.split(" "))

#remover caracteres do inicio e do fim
nome2 = "xVictor Ferreirax"
print(nome2.strip("x"))
print(nome2.rstrip("x"))

#Comparadores
print(nome_completo.startswith("Vi"))
print(nome_completo.startswith("Be"))

print("Vi" in nome_completo)
print("Es" not in nome_completo)