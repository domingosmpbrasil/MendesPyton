# Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato
# faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


ganho_por_hora = float(input("Digite aqui quanto você ganha por hora: "))
horas_por_dia = int(8)
desconto_ir = 11.0 / 100
desconto_inss = 8.0 / 100
desconto_sindicato = 5.0 / 100


salario_bruto = (ganho_por_hora * horas_por_dia) * 22
valor_do_ir = (desconto_ir * salario_bruto)
valor_inss = (desconto_inss * salario_bruto)
valor_sindicato = (desconto_sindicato * salario_bruto)
valor_salario_liquido = salario_bruto - (valor_do_ir + valor_inss + valor_sindicato)


print(f'Seu salário bruto mensal é de: {salario_bruto}, ------ você vai pagar de imposto de renda: {valor_do_ir}, ------ o valor descontado do INSS é de: {valor_inss}, ------ o desconto do sindicato é de: {valor_sindicato}, ------ Seu salário líquido é de: {valor_salario_liquido:.2f}')


