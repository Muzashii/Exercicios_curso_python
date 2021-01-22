"""
mostrar quel numero é maior
"""

numero1 = float(input(f'Digite dois numeros e o programa te retornara o maior.\nPrimeiro Numero:'))
numero2 = float(input(f'Segundo Numero:'))


if numero1 > numero2:
    print(numero1)
elif numero1 == numero2:
    print(f'Numeros iguais')
else:
    print(numero2)
