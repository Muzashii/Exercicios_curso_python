"""
numero par ou impar
"""

numero = int(input(f'Digite um numeros e o programa te retornara se ele e par ou impar\nDigite um Numero:'))

resultado = numero % 2

if resultado >= 1 :
    print(f'O numero {numero} é impar')
else:
    print(f'O numero {numero} é par')
