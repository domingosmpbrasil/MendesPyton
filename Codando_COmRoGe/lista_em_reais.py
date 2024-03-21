reais = []

for i in range(5):
    reais.append(float(input("Digite o valor Em reais: ")))

    if reais[i] > 100:
        acrecenta = float(reais[i] * 5 / 100)
        soma = reais[i] + acrecenta
        print(f'o ndumero digitado foi: {reais[i]} com acréscimo de 05 % ede: {acrecenta:.2f} O valor final é de: {soma}')

    if reais[i] <= 100:
        acrecenta = round((reais[i] * 10 / 100), 2)
        soma = reais[i] + acrecenta
        print(f'o numero digitado foi: {reais[i]} com acréscimo de 10 % ede: {acrecenta} E o valor final é de: {soma}')
