
verificando_Numero = float(input("Digite o Número, vamos ver se ele é, negativo ou positivo: "))

if (verificando_Numero % 2 != 0):
    print(f' O número R$: {verificando_Numero} é impa.')
else:
    print(f'O Número R$: {verificando_Numero} é par.')

if (verificando_Numero < 0):
    print(f' e ele é negativo: ')
else:
    print(f' E ele é Positivo: ')