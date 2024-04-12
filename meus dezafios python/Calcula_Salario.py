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
# Remover a conversão de numeros pois não há necessidade sendo que o python já reconhece e adere o tipo do valor que vc atribui para a variável. 
horas_por_dia = int(8)
# Sugesstão: Sabendo que os valores serão calculados em porcentagem vc precisa fazer a conversão, sendo assim pode fazer a conversão dentro da propria variável dividindo o valor por 100.
# Somente fará isso se estiver trabalhando com porcentagem OK. IR, INSS e SINDICATO são porcentagens.  
desconto_ir = float(11)
desconto_inss = float(8)
desconto_sindicato = float(5)


salario_bruto = float(ganho_por_hora * horas_por_dia) * 22
valor_do_ir = float(desconto_ir * salario_bruto) / 100
valor_inss = float(desconto_inss * salario_bruto) / 100
valor_sindicato = float(desconto_sindicato * salario_bruto) / 100
valor_salario_liquido = float(salario_bruto - valor_do_ir - valor_inss - valor_sindicato)

# Sugestão: Casos queira para ficar com um visual melhor pode definir um print para cada campo. Dessa forma a linha de retorno fica muito grande e visualmente ruim pra poder enxergar OK.  
print(f'Seu salário bruto mensal é de: {salario_bruto}, ------ você vai pagar de imposto de renda: {valor_do_ir}, ------ o valor descontado do INSS é de: {valor_inss}, ------ o desconto do sindicato é de: {valor_sindicato}, ------ Seu salário líquido é de: {valor_salario_liquido:.2f}')


