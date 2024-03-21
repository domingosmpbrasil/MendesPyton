lista1 = [10, 20, 30, 40, 50]
lista2 = [10, 20, 60, 70]

print(lista1)
print(lista2)
print(50*"=")
print()

# transformando lista em set
num1 = set(lista1)
num2 = set(lista2)

print(num1)

# Union (União)  = unindo duas listas e escluindo repetições.
print(num1 | num2)

# Difference (diferença) = uni as duas listas excluindo o que é igual.
print(num1 - num2)

# Symetric difference (diferença symetrica) = uni duas tabelas removendo das duas os repetidos.
print(num1 ^ num2)

# and (e) = mostra somente o que estar repetido nas duas listas.
print(num1 & num2)

# len (quantidade) = mostra quantidade de itens no set.
print(len(num1))