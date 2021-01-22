"""
salario valido ou nao
"""
salario = float(input(f'Digite seu salario e o valor do emprestimo, para ver se ele sera aprovado:\n'
                      f'Valor do salario: '))
emprestimo = float(input(f'Digite o valor do emprestimo: '))
vint = salario * 0.2

if emprestimo > vint:
    print(f'o emprestimo nao foi aprovado')
else:
    print(f'O emprestimo foi aprovado')
