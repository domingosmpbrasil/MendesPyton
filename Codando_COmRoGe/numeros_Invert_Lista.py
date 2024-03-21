lista = []
# iniciando as variaveis com valor 0
maior = 0
menor = 0

# incerindo as informações dentro da lista.
for c in range(0, 5):
    lista.append(input("digite o número: "))

# pecorrendo a lista em busca do maior e menor valor incerido.
for c, numeros in enumerate(lista):

    # Se contador for igual a 0 atribua o valordo primeiro item da lista.
    # as duas variaveis maior e menor.
    if c == 0:
        maior = menor = lista[c]
    else:
        # Verifica pecorrendo as posições qual é o maior número.
        if lista[c] > maior:
            maior = lista[c]

        # verifica pecorrendo as posições qual é o menor número
        if lista[c] < menor:
            menor = lista[c]

# Busca dentro da lista se existe o valor especificado
if maior in lista:
    print(f'Maior número: {maior} na posição {lista.index(maior)}')

if menor in lista:
    print(f'Menor número: {menor} na posição {lista.index(menor)}')
