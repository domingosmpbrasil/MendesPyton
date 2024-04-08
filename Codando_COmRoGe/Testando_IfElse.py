entrada = float(input("digite a nota do aluno: "))

if entrada > 10 or entrada < 0:
    print(f'Entrada inválida: ')
else:
    if entrada >= 8:
        print(f'Parabéns você foi aprovado com Lovor: {entrada}, essa é sua nota" ')
    elif entrada >= 6:
        print(f'Boa! Você foi bem:')
    else:
        print(f'Que pena! não foi dessa vez, Você perdeu:')
