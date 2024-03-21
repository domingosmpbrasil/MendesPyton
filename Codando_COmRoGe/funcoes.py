
#função criadas sem receber parâmetros
def somar_dois_numeros():
    primeiro_numero = 10
    segundo_numero = 5
    soma = primeiro_numero + segundo_numero
    print(soma)

somar_dois_numeros()

#função criada recebendo parâmetro

def somar(n1, n2):
    soma = n1 + n2
    print(f'A soma do número {n1} + {n2} = {soma}')


primeiro_numero = int(input("digite o primeiro número:"))
segundo_numero = int(input("digite o segundo número:"))

somar(primeiro_numero, segundo_numero)
somar(100, 50)