primeiro_Numero = int(input("Digite o primeiro Número: "))
segundo_Numero = int(input("Digite o Segundo Número: "))
terceiro_Numero = int(input("Digite o terceiro Número: "))
print("o Primeiro número é: ", primeiro_Numero)
print("O Segundo Número é:", segundo_Numero)
print("O terceiro Número é: ", terceiro_Numero)

print("Agora vamos inverter esses Números... ")
print()

if (terceiro_Numero > segundo_Numero):
    numero_invertido = terceiro_Numero
    terceiro_Numero = segundo_Numero
    segundo_Numero = numero_invertido

if(segundo_Numero > primeiro_Numero):
    numero_invertido = segundo_Numero
    segundo_Numero = primeiro_Numero
    primeiro_Numero = numero_invertido

if(terceiro_Numero > segundo_Numero):
    numero_invertido = terceiro_Numero
    terceiro_Numero = segundo_Numero
    segundo_Numero = numero_invertido

print("o Primeiro número é: ", primeiro_Numero)
print("O Segundo Número é:", segundo_Numero)
print("O terceiro Número é: ", terceiro_Numero)
