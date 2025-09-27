def adicionar_item(nome_do_item, quantidade_de_items):
    items = {"nome": nome_do_item, "quantidade": quantidade_de_items}
    lista.append(items)
    print(f"Você adicionou {quantidade_de_items}x {nome_do_item} a lista de compras!")
    return

#def remover_items()




lista = []

while True:
    print("Lista de compras: ")
    print("1. Adicionar Item")
    print("2. Remover Item")
    print("3. Ver lista")
    print("4. Sair")

    resposta = input("Digite a sua escolha: ")


    if resposta == "1":
        nome_do_item = input("Digite o nome do item: ")
        quantidade_de_items = input(f"Digite a quantidade de {nome_do_item}: ")
        adicionar_item(nome_do_item, quantidade_de_items)