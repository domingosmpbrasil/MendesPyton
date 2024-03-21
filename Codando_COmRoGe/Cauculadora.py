print("Olá tem uma continha para fazer? não se preocupe! é só digitar aqui que eu farei para você!😊😊")
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o cegundo número:"))

print("O que você quer fazer? 1 - Adição, 2 - Subtração, 3 - Multiplicação, 4 - Divisão. ")
pergunta = int(input("Digite a sua opção:"))

match pergunta:
    case 1:
        adicao = primeiro_numero + segundo_numero
        print(f'{primeiro_numero}, mais: {segundo_numero}, igual A: ', adicao)
    case 2:
        subtracao = primeiro_numero - segundo_numero
        print(f'{primeiro_numero}, Menos {segundo_numero} igual a:', subtracao)
    case 3:
        mutiplicacao = primeiro_numero * segundo_numero
        print(f'{primeiro_numero}, Vezes {segundo_numero} igual A: ', mutiplicacao)
    case 4:
        divizao = primeiro_numero / segundo_numero
        print(f'{primeiro_numero} Dividido por: {segundo_numero} Igual a:', divizao)
    case _:
        print("Operação errada! 😢 escolha umas das opções assima 1,, 2, 3 ou 4.")
