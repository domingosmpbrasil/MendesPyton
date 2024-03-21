# Calcula o valor de uma compra de blocos

# Declaração das variáveis
bloco = int(input("Quantos Blocos você quer? "))
valorDe_Cada_Bloco = float(input("quanto custa cada bloco? "))
desconto = valorDe_Cada_Bloco * 10.00

# Calcula o valor total dos blocos
somando_ValorDos_Blocos = bloco * valorDe_Cada_Bloco

# Imprime o valor total dos blocos
if (bloco < 1000):
    print(f'O valor dos Blocos é: {somando_ValorDos_Blocos}')
else:
    print(f'O valor dos blocos foi: {somando_ValorDos_Blocos - desconto}')
