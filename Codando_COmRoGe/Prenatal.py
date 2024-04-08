semanas = int(input("Digite o número de semanas de gravidez: "))
dias = semanas * 7
meses = dias / 30

if (meses == 9):
    print("Parabéns, hoje é o mês do nascimento!!! ")
elif (meses >=6 and meses< 9):
    print("bo ai mamãe está quase lá.")
elif (meses >= 1 and meses < 6):
    print("Muito bem continue se cuidando")
