nota1_Aluno = float(input("Digite a Primeira nota: "))
nota2_Aluno = float(input("Digite a segunda nota: "))
nota3_Aluno = float(input("Digite a terceira nota:"))
nota4_aluno = float(input("Digite a quarta nota:"))
media = float(nota1_Aluno + nota2_Aluno + nota3_Aluno + nota4_aluno) / 4

if (media < 6):
    print(f'Você foi reprovado! estuda mais um pouquinho!: ')
if (media >= 6):
    print(f'Parabéns Você foi aprovado!👏👏: ')
