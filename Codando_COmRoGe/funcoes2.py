
#Função sem receber parametros.
def nome_funcao():
    print("Olá!")

nome_funcao()

#Função sem parametros mas com retorno
def soma():
    numero1 = 10
    numero2 = 5
    soma = numero1 + numero2
    return soma

print(soma())

#Função que recebe dois números com parametros e retorna a soma desses dois números.
def soma_dois_numeros(numero1, numero2):
    soma = numero1 + numero2
    return soma

print(soma_dois_numeros(20, 30))