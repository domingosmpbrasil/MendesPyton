#Cria uma função que receba dois números e os mutiplique.



#def soma_dois_numeros():
#    n1 = int(input("Digite o primeiro número: "))
#    n2 = int(input("Digite o segundo número: "))

#    soma = n1 + n2
#    return soma

#print(soma_dois_numeros())



#Cria uma função que faça uma menssagem de boas vindas, nessa menssagem você pode colocar um nome qualquer,
#porem sem parametros.

#def mensagem():
    #print(f"ceja bem vindo! , Fique com a gente! aqui é bom de mais!💖")

#mensagem()



#Crie uma função que receba o nome e sobrenome de uma pessoa, e retorne o nome completo da pessoa.



nome = str(input("Escreva o seu nome: "))
sobrenome = str(input("Agora digite o sobrenome: "))

def nome_sobrenome(nome, sobrenome):
    return nome + sobrenome

print("Olá bem vindo de volta! ", nome_sobrenome(nome, sobrenome))
