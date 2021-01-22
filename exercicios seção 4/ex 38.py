"""
aumento de 25% de salario
"""
sala = float(input(f"Digite o valor do salari que deseja almentar em 25%\nDigite o valor do salario: R$"))

bonus = sala * 0.25

final = sala + bonus

print(f'Com o salario de R${sala} se tem um almento de R${bonus} que da um novo salario de R${final}')
