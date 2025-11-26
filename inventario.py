inventario = []

while True:
    print("Bem vindo ao inventário: 1.Adicionar item, 2.Remover item, 3. Listar inventário, 4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do item: ")
        try:
            quantidade = int(input("Quantidade: "))
            inventario.append({"nome": nome, "quantidade": quantidade})
        except ValueError:
            print("Quantidade inválida.")
    elif opcao == "2":
        print (f"Itens no inventário: {[item['nome'] for item in inventario]}")
        nome = input(f"Nome do item a remover: ")
        inventario = [item for item in inventario if item["nome"].lower() != nome.lower()]
    elif opcao == "3":
        if inventario:
            for i, item in enumerate(inventario, 1):
                print(f"{i}. {item['nome']} - {item['quantidade']}")
        else:
            print("Inventário vazio.")
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
        