soma = 0
cont = 0

for contador in range(1, 501):

    if contador % 2 == 1 and contador % 3 == 0:
        #soma = soma + contador (pode ser representado igual abaixo)
        soma += contador
        cont += 1

print(f'a somatora dos Números impares e divizives por 3 é {soma}')
print(f'A quantidade de números encontrados foi: {cont}')