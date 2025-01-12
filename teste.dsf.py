lista_produtos = []
saldo = 0

def mostrar():
    if not lista_produtos:
        print("O estoque está vazio.")
        return
    
    for idx, produto in enumerate(lista_produtos, 1):
        print(f"\n{idx}° produto")
        print(f"Nome: {produto['nome']}")
        print(f"ID: {produto['id']}")
        print(f"Preço: {produto['preço']} reais")
        print(f"Unidades disponíveis: {produto['disponiveis']}")

def cadastrar():
    print("Você pode cadastrar no máximo 5 produtos por vez.")
    print()

    for _ in range(5):
        if len(lista_produtos) >= 100:
            print("O limite de 5 produtos foi atingido.")
            break

        continua = input("Você quer cadastrar um novo produto? (s/n): ").strip().lower()
        if continua == "n":
            break
        elif continua == "s":
            produto = {}
            produto["id"] = int(input("Qual o ID do produto? "))
            produto["nome"] = input("Qual o nome do produto? ")
            produto["preço"] = float(input("Qual o preço do produto? "))
            produto["disponiveis"] = int(input("Quantas unidades estão disponíveis? "))
            lista_produtos.append(produto)
            print("\nProduto cadastrado com sucesso!")
            mostrar()
        else:
            print("Opção inválida.")

def procurar():
    if not lista_produtos:
        print("O estoque está vazio.")
        return

    busca = input("Digite o nome ou ID do produto que deseja encontrar: ").strip()
    encontrado = False
    for produto in lista_produtos:
        if busca == produto["nome"] or busca == str(produto["id"]):
            print("\nAqui estão os dados do produto:")
            print(f"Nome: {produto['nome']}")
            print(f"ID: {produto['id']}")
            print(f"Preço: {produto['preço']} reais")
            print(f"Unidades disponíveis: {produto['disponiveis']}")
            encontrado = True
            break
    if not encontrado:
        print("Produto não encontrado.")

def vender():
    if not lista_produtos:
        print("O estoque está vazio.")
        return

    venda = input("Digite o nome ou ID do produto que deseja vender: ").strip()
    for produto in lista_produtos:
        if venda == produto["nome"] or venda == str(produto["id"]):
            print("\nAqui estão os dados do produto:")
            print(f"Nome: {produto['nome']}")
            print(f"ID: {produto['id']}")
            print(f"Preço: {produto['preço']} reais")
            print(f"Unidades disponíveis: {produto['disponiveis']}")
            vqnt = int(input(f"Quantas unidades você quer vender? (máximo {produto['disponiveis']}): "))
            if 0 < vqnt <= produto['disponiveis']:
                produto['disponiveis'] -= vqnt
                print("\nVenda realizada com sucesso!")
                global saldo
                saldo += (produto['preço'])*vqnt
            else:
                print("Quantidade inválida.")
            return
    print("Produto não encontrado.")

def alterar():
    if not lista_produtos:
        print("O estoque está vazio.")
        return

    busca = input("Digite o nome ou ID do produto que deseja alterar: ").strip()
    for produto in lista_produtos:
        if busca == produto["nome"] or busca == str(produto["id"]):
            print("\nAqui estão os dados do produto:")
            print(f"Nome: {produto['nome']}")
            print(f"ID: {produto['id']}")
            print(f"Preço: {produto['preço']} reais")
            print(f"Unidades disponíveis: {produto['disponiveis']}")

            while True:
                print("\nO que você deseja alterar?")
                print("1. Nome")
                print("2. Preço")
                print("3. Estoque")
                print("4. Voltar ao menu principal")
                
                opcao = input("Escolha uma opção: ").strip()
                if opcao == "1":
                    novo_nome = input("Digite o novo nome: ").strip()
                    produto["nome"] = novo_nome
                    print("Nome alterado com sucesso!")
                elif opcao == "2":
                    try:
                        novo_preco = float(input("Digite o novo preço: "))
                        if novo_preco < 0:
                            print("O preço deve ser um valor positivo.")
                        else:
                            produto["preço"] = novo_preco
                            print("Preço alterado com sucesso!")
                    except ValueError:
                        print("Por favor, insira um número válido.")
                elif opcao == "3":
                    try:
                        novo_estoque = int(input("Digite o novo estoque: "))
                        if novo_estoque < 0:
                            print("O estoque deve ser um valor positivo.")
                        else:
                            produto["disponiveis"] = novo_estoque
                            print("Estoque alterado com sucesso!")
                    except ValueError:
                        print("Por favor, insira um número inteiro válido.")
                elif opcao == "4":
                    print("Voltando ao menu principal.")
                    return
                else:
                    print("Opção inválida. Tente novamente.")
            return
    print("Produto não encontrado.")

while True:
    print("\nO que você deseja fazer?")
    print("1 - Cadastrar novos produtos")
    print("2 - Procurar produto")
    print("3 - Exibir estoque")
    print("4 - Fazer uma venda")
    print("5 - Alterar produto")
    print("6 - Mostrar Saldo")
    print("7 - Desligar o sistema")

    escolha = input("Escolha uma opção: ").strip()
    if escolha == "1":
        cadastrar()
    elif escolha == "2":
        procurar()
    elif escolha == "3":
        mostrar()
    elif escolha == "4":
        vender()
    elif escolha == "5":
        alterar()
    elif escolha == "6":
        print(f"Seu saldo atual é R${saldo}")
    elif escolha == "7":
        print(f"Você fechou o dia com R${saldo}")
        print("Sistema desligado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
