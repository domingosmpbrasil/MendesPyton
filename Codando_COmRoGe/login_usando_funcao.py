
print('############ Digite seu usuário e senha para acessar o sistema. ###################\n')

usuario_list = []
senha_list = []

# Validação de usuário e senha com funções
def cadastrar_nome(lista_nomes, novo_nome):

    if novo_nome in lista_nomes:
        print("Nome já existe! Por favor, insira um nome diferente.")
    else:
        lista_nomes.append(novo_nome)
        cadastrar_senha()
        print("Usuário e senha cadastrado com sucesso!!!")

def cadastrar_senha():
    senha = input("Digite a senha: ")
    senha_list.append(senha)


# Cadastro de usuário e senha
while True:
    cadastro = input('Deseja cadastrar novo usuário? (S/N)').lower()

    if cadastro == 'n':
        print()
        break

    nome = input("Digite um nome do Usuário: ").lower()

    cadastrar_nome(usuario_list, nome)

# Login para acesso no sistema
print('################## FAÇA SEU LOGIN ##################\n')

cont = 0
finaliza = True
while finaliza:

    usuario = input('Digite seu Usuário: ').lower()
    senha = input('Digite sua senha: ').lower()

    for valor in usuario_list:
        if valor == usuario:

            for valor_senha in senha_list:

                if valor_senha == senha:
                    print('Usuário logado e OK!!!')
                    input('Pressione ENTER para sair...')
                    finaliza = False

                else:
                    print('Usuário ou senha incorreto digite novamente!!!\n')
                    cont += 1

                    if cont == 3:
                        print('Vc fez 3 tentativas e bloqueou seu acesso!!!')
                        finaliza = False
                        break

                    continue
        else:
            print('Usuário ou senha incorreto digite novamente!!!\n')
            cont += 1

            if cont == 3:
                print('Vc fez 3 tentativas e bloqueou seu acesso!!!')
                finaliza = False
                break

            continue

        finaliza = False