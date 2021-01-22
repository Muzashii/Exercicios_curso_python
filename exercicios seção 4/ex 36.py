"""
descobrir o volume de um cilindro
"""
alt = float(input(f'Digite a altura e o raio de um cilindro para obter seu volime\nDigite a altura: '))
raio = float(input(f'Digite o raio: '))

v = 3.141592 * (raio ** 2) * alt

print(f'O volume do cilindro de altura = {alt} metros e raio = {raio} metros é de {v} metros quadrados')