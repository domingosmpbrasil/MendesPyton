print("opção 1")
print("opção 2")
print("opção 3")
print("opção 4")

opcao = int(input("Digite uma opção: "))

match opcao:
    case 1:
        print("Você escolheu a opção 1.")

    case 2:
        print("Você escolheu a opção 2.")

    case 3:
        print("Você escolheu a opção 3")

    case 4:
        print("Você escolheu a opção 4.")

    case _:
        print("Escolha invalida.")