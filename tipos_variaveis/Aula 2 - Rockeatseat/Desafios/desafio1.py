#Código pronto

def adicionar_contato(nome_do_contato, telefone_do_contato, email_do_contato):
    contato = {"nome":nome_do_contato, "telefone": telefone_do_contato, "email": email_do_contato, "favoritado":False}
    agenda.append(contato)
    print(f"Contato {nome_do_contato} foi salvo com sucesso!")
    return

def ver_contatos(agenda):
    print("\nLista de contatos:")
    for indice, contato in enumerate(agenda,start=1):
        status = "♥" if contato["favoritado"] else " "
        nome_do_contato = contato["nome"]
        telefone_do_contato = contato["telefone"]
        email_do_contato = contato["email"]
        print(f"{indice}. [{status}] {nome_do_contato}, {telefone_do_contato}, {email_do_contato}")
    return

def editar_contato(agenda, indice_contato, novo_nome, novo_telefone, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
        agenda[indice_contato_ajustado]["nome"] = novo_nome
        agenda[indice_contato_ajustado]["telefone"] = novo_telefone
        agenda[indice_contato_ajustado]["email"] = novo_email
        print(f"O contato {novo_nome} foi editado com sucesso!")
    else:
        print("O índice do contato é inválido")
    return

def favoritar_contato(indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    nome = agenda[indice_contato_ajustado]["nome"]
    if agenda[indice_contato_ajustado]["favoritado"] == False:
        agenda[indice_contato_ajustado]["favoritado"] = True
        print(f"Contato {nome} foi favoritado")
    else:
        agenda[indice_contato_ajustado]["favoritado"] = False
        print(f"Contato {nome} foi removido dos favoritos")
    return

def ver_favoritos(agenda):
    print("\nLista de contatos favoritos:")
    encontrou = False
    for indice, contato in enumerate(agenda, start=1):
        if contato["favoritado"]:
            encontrou = True
            nome_do_contato = contato["nome"]
            telefone_do_contato = contato["telefone"]
            email_do_contato = contato["email"]
            print(f"{indice}. [♥] {nome_do_contato}, {telefone_do_contato}, {email_do_contato}")
    
    if not encontrou:
        print("Nenhum contato foi favoritado ainda.")
    return

def apagar_contato(agenda, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
        contato = agenda[indice_contato_ajustado]
        nome = agenda[indice_contato_ajustado]["nome"] 
        agenda.remove(contato)
        print(f"O contato {nome} foi excluído com sucesso!")
    else:
        print("O índice do contato é inválido")
    return

agenda = [
    {"nome": "Ana Silva", "telefone": "91234-5678", "email": "ana@email.com", "favoritado": False},
    {"nome": "Bruno Costa", "telefone": "98765-4321", "email": "bruno@email.com", "favoritado": True},
    {"nome": "Carla Souza", "telefone": "92345-6789", "email": "carla@email.com", "favoritado": False},
    {"nome": "Sergio Costa", "telefone": "98765-4321", "email": "bruno@email.com", "favoritado": True},
    {"nome": "Carmem Paixão", "telefone": "92345-6789", "email": "carla@email.com", "favoritado": True}
]

while True:
    print("\n --- Agenda Telefonica ---")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar um contato")
    print("4. Favoritar um contato")
    print("5. Ver contatos favoritos")
    print("6. Apagar um contato")
    print("7. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_do_contato = input("Digite o nome do contato: ")
        telefone_do_contato = input("Digite o numero de contato: ")
        email_do_contato = input("Digite o Email do contato: ")
        adicionar_contato(nome_do_contato, telefone_do_contato, email_do_contato)        
    
    elif escolha == "2":
        ver_contatos(agenda)
    
    elif escolha == "3":
        ver_contatos(agenda)
        indice_contato = input("Digite o numero do contato que deseja editar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        novo_email = input("Digite o novo email do contato: ")
        editar_contato(agenda, indice_contato, novo_nome, novo_telefone, novo_email) 

    elif escolha == "4":
        ver_contatos(agenda)
        indice_contato = input("Qual o contato que deseja favoritar?")
        favoritar_contato(indice_contato)

    elif escolha == "5":
        ver_favoritos(agenda)
            
    elif escolha == "6":
        indice_contato = input("Qual o contato que deseja apagar?")
        apagar_contato(agenda, indice_contato)

    elif escolha == "7":
        break
    