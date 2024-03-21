
var1 = int(input('Primeiro numero: '))
var2 = int(input('Segundo numero : '))
var3 = int(input("Terceiro número: "))
var4 = int(input('Quarto Número: '))

print('Variavel 1: ', var1)
print('Variavel 2: ', var2)
print('variavel 3: ', var3)
print('Variavel 4: ', var4)
print('Invertendo...')

aux = var2
var2 = var1
var1 = aux
aux = var3
var3 = var2
var2 = aux
aux = var4
var4 = var1
var1 = aux

print('Variavel 1: ', var1)
print('Variavel 2: ', var2)
print('variavel 3: ', var3)
print('Variavel 4: ', var4)

