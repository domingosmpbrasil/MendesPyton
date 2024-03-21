cont = 0

while True:
    nome_de_usuario = input("Digite o nome do usuário: ").lower()
    senha = input("Digite a senha:")

    if nome_de_usuario == "pedro" and senha == "amigo":
        print("Bem vindo! ", nome_de_usuario.upper(), "Login realizado")
        break
    else:
        cont = cont + 1
        print("Usuário ou senha incorretos!!!\n")
        if cont == 3:
            print("Usuário digitou 3 vezes e esta bloqueado")
            break
        finaliza = input("quer continuar? (s/n)")
    if finaliza == "s":
        print("digite mais uma vez:")
    else:
        print("Fim do programa!")
        break

cont = 0

while True:
    nome_de_usuario =input("Digite o nome do usuário: ").lower()
    senha =input("Digite a senha:")
    if nome_de_usuario == "pedro" and senha == "amigo":
        print("Bem vindo! ", nome_de_usuario.upper(),"Login realizado")
        break
    else:
        cont = cont + 1
        print("Usuário ou senha incorretos!!!\n")
        if cont == 3:
            print("Vc fez 3 tentativas e está bloqueado!!!")
            break
        else:
            finalizar = input("Deseja digitar novamente? (S/N)")
            if finalizar == 's':
                continue
            else:
                break