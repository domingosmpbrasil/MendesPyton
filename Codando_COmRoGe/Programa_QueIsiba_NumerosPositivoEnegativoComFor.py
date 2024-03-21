lista = [10, 21, 32, 135, 98, -5, -12, -59, -48, -189]

for contador in range(0, 10):
    if lista[contador] >= 0:
        print(f'O número {lista[contador]} é positivo.')
        if lista[contador] % 2 != 0:
            print(f'O número {lista[contador]} é impar.')
        else:
            print(f'O número {lista[contador]} é par.')


    if lista[contador] < 0:
        print(f' o número {lista[contador]} é negativo.')
    if lista[contador] % 2 == 1:
        print(f'o número {lista[contador]} é impa')
    else:print(f' e o número {lista[contador]} é par')