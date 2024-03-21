lista = ["Miguel", 55, 44.5, 10 > 5]
print(lista)

for c in range(0, 4):
    print(f'{lista[c]}, Sua posição {lista.index(lista[c])}, Tipo de dados {type(lista[c])}')
