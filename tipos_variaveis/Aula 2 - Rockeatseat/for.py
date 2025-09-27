lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

pessoa = {"nome": "joão", "idade": "25", "cidade": "São Paulo"}
print("For utilizando dicionário - chaves")
for chave in pessoa.keys():
    print(chave)

print("For utilizando dicionário - valores")
for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# range(): intervalo númerico
# [0,1,2,3,4,5,6,7,8,9]

range(0,10)
list(range(0,10))

print("\nUtilizando a função range()")
for numero in range(0,5):
    print("Numero:", numero)


print("\nUtilizando a função range() com len()")
lista = [1,2,3,4,5]
for indice in range(0, len(lista)):
    print("Indice:", indice)
    print("Elemento:", lista[indice])
    if indice == 3:
        lista[indice] = 5
print(lista)


# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate():
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")