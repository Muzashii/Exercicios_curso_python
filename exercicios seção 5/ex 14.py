"""
media ponderada de 3 provas
"""
nota1 = float(input(f'Digite a nota de 3 provas e recebera a mdia ponderda:\n Nota do trabalho: '))
nota2 = float(input(f'Nota da avaliação: '))
nota3 = float(input(f'Nota do exame final: '))

trabalho = nota1 * 2
avaliaçao = nota2 * 3
exame = nota3 * 5
media = (trabalho + avaliaçao + exame) / 10

if media >= 5:
    print(f'Com uma nota de {media} o aluno foi aprovado')
elif media >= 3:
    print(f'Com a nota de {media} o aluno esta de recuperação')
else:
    print(f'com uma nota de {media} o aluno foi reprovado')
