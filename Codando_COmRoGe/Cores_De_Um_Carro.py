print("Seja bem vindos! escolha a cor de seu carro e boa compra! ")

print('Opção 1: Vermelho, - Opição 2: Azul, - Opição 3: Branco, - Opição: 4: Preto.')

cores = int(input("Digite o número de sua cor Preferida: "))

match cores:
    case 1:
        print("Você escolheu a cor Vermelha! ")

    case 2:
        print("Você escolheu a cor Azul! ")

    case 3:
        print("Você escolheu a cor Branca! ")

    case 4:
        print("Você escolheu a cor Preta!")

    case _:
        print("Erro escolha entre as Opção 1, 2 3 e 4!")