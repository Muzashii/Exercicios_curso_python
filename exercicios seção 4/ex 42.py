"""
salario final de um funcionario
"""
salario = float(input(f'Digite o valor do salario-base do funcionario:\nSalario do funcionario R$'))

add = salario * 0.05
salarioadd = salario + add

impos = salario * 0.07
salariofinal = salarioadd - impos

print(f'Com um salario base de R${salario}, ele recebe um bonus de R${add} e paga R${impos} em impostos, tendo no'
      f' final um salariop de R${salariofinal}')
