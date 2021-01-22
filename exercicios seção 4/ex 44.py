"""
contador da altura da escada
"""

degrau = float(input(f'Digite a altura dos degraus e a altura que deseja alcançar:\nDigite a altura do degrau:'))
altura = float(input(f'Digite a altura que deseja alcançar:'))

total = altura / degrau

print(f'Para chegar na altura de {altura} serao nescessarios {total} degraus')
