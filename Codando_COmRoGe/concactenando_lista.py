lista1 = [1, 2, 3, 4, 5]
lista2 = ['a', 'b', 'c', 'd', 'e']

# duplicando uma lista
duplicando = lista1 * 2
print("lista duplicada: ", duplicando)

# concactenando lista.
juntando = lista1 + lista2
print("lista concactenada: ", juntando)


lista1.extend(lista2)
print(lista1)