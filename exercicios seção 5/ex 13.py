"""
media ponderada de 3 provas
"""
nota1 = float(input(f'Digite a nota de 3 provas e recebera a mdia ponderda:\n Primeria nota: '))
nota2 = float(input(f'Segunda nota: '))
nota3 = float(input(f'Terceira nota: '))

nota4 = nota3 * 2
media = (nota1 + nota2 + nota4) / 4

if media >= 60:
    print(f'Com uma nota de {media} o aluno foi aprovado')
else:
    print(f'com uma nota de {media} o aluno foi reprovado')
