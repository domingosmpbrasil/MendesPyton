print("Seja todos bem vindos a loja do mendes! Aqui temos tudo que você procura por um preço imperdível! ❤❤❤")
print("1 Eletrônicos, - 2 Eletrodomésticos, - 3 Moveis para Casa - 4 Cama, Mesa e Banho. - ")
pergunta_Ao_Cliente = int(input("O que você deseija? digite sua opção: "))

match pergunta_Ao_Cliente:
    case 1:
        escolha_Cliente = str(input("Para prosseguirmos com a compra, precisamos de fazer o seu cadastro deseja se cadastrar? Digite s para sim ou n para não. "))
        if escolha_Cliente == "s":
            nome = str(input("digite seu nome: "))
            indereco = str(input("Digite seu indereço: "))
            telefone = int(input("Digite seu telefone: "))
            print(f' bem vindo {nome} cadastro realisado com sucesso! 😊seja bem vindo e boas compras.')
        else:
            print("😢😢 infelismente não podemos seguir com a compra sem o seu cadastro. ")
    case 2:

            escolha_Cliente = str(input("Para prosseguirmos com a compra, precisamos de fazer o seu cadastro deseja se cadastrar? Digite s para sim ou n para não. "))
            if escolha_Cliente == "s":
                nome = str(input("digite seu nome: "))
                indereco = str(input("Digite seu indereço: "))
                telefone = int(input("Digite seu telefone: "))
                print(f' bem vindo {nome} cadastro realisado com sucesso! 😊seja bem vindo e boas compras. ')
            else:
                print("😢😢 infelismente não podemos seguir com a compra sem o seu cadastro. ")
    case 3:

            escolha_Cliente = str(input("Para prosseguirmos com a compra, precisamos de fazer o seu cadastro deseja se cadastrar? Digite s para sim ou n para não. "))
            if escolha_Cliente == "s":
                nome = str(input("digite seu nome: "))
                indereco = str(input("Digite seu indereço: "))
                telefone = int(input("Digite seu telefone: "))
                print(f' bem vindo {nome} cadastro realisado com sucesso! 😊seja bem vindo e boas compras. ')
            else:
                print("😢😢 infelismente não podemos seguir com a compra sem o seu cadastro. ")
    case 4:

        escolha_Cliente = str(input("Para prosseguirmos com a compra, precisamos de fazer o seu cadastro deseja se cadastrar? Digite s para sim ou n para não. "))
        if escolha_Cliente == "s":
            nome = str(input("digite seu nome: "))
            indereco = str(input("Digite seu indereço: "))
            telefone = int(input("Digite seu telefone: "))
            print(f' bem vindo {nome} cadastro realisado com sucesso! 😊seja bem vindo e boas compras. ')
        else:
            print("😢😢 infelismente não podemos seguir com a compra sem o seu cadastro. ")
    case _:
        print("OPS só validamos as opções de 1 a 4. escolha uma dessas opções para proceguirmos! ")