"""
Calculo da hora de trabalho/valor da hora de trabalho
"""
valor = float(input(f'Digite o valor da hora trabalhada e o numero de horas trabalhadas no mes:\nValor da hora '
                    f'trabalhada: '))
hora = int(input(f'Horas trabalhadas no mes: '))

cal = valor * hora
por = cal * 0.01
final = cal + por

print(f'Com um total de {hora} horas de trabalho, com cada hora valendo R${valor} se tem um total de R${cal}'
      f', com mais 10% se tem R${final}')
