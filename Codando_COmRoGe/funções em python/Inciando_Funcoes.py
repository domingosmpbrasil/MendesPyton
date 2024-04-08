# sintaxe da função:
# def - palavra resevada do python para criação de uma função
# nome_da_funcao - nome dado a função
# ( ) - local onde declaro os parametros
# : - finaliza a escrita da função, na proxima linha com indentação de quatro espaços começa o bloco de código da função

# função sem parametro
def soma_dois_numeros():
    primeiro_numero = 20
    segundo_numero = 15
    resultado = primeiro_numero + segundo_numero
    return resultado

# função recebendo parametros
def somar(primeiro_numero, segundo_numero):

    return primeiro_numero + segundo_numero

def retornar_texto():
    return ""