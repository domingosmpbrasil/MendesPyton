nomes_de_pessoas = []

for contador in range(3):
    nomes_de_pessoas.append(input("Digita o Nome da pessoa: "))


for contador in range(0, 3):
    #print(f'O nome {nomes_de_pessoas[contador]} está na posição {nomes_de_pessoas.index(nomes_de_pessoas[contador])}')
    print(nomes_de_pessoas.index(nomes_de_pessoas[contador]))
