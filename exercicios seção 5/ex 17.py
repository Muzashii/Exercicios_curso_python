"""
calcular area de trapezio
"""

basema = float(input(f'Digite o valor da altura, da base maior e da base menos de um trapezio para receber a area:'
                     f'\nBase maior:'))
baseme = float(input(f'Base menor:'))

altu = float(input(f'altura:'))
if basema >= 0 or baseme >= 0:
    print(f'numero invalido')
else:
    area = ((basema + baseme) * altu) / 2
    print(f'area total {area}')
