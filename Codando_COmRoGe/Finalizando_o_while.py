nome = "S"

while nome.lower() == "s":
    print("Olá")
    nome = input("Deseja finalisar o programa? (S/N)")
    if nome == "s":
        print("Finalizando o programa... ")
        break
    else:
        nome = "s"
        print("Continuando com o programa...")


print("Programa finalizado!")