"""
mostrar quel numero é maior
"""

numero1 = float(input(f'Digite dois numeros e o programa te retornara o maior.\nPrimeiro Numero:'))
numero2 = float(input(f'Segundo Numero:'))


if numero1 > numero2:
    dif = numero1 - numero2
    print(f'O numero {numero1} é maior, tendo uma diferença de {dif} para o numero {numero2} ')
else:
    dif2 = numero2 - numero1
    print(f'O numero {numero2} é maior, tendo uma diferença de {dif2} para o numero {numero1} ')
