"""
 raiz de numero possitivo
"""

numero1 = float(input(f'Digite um numeros e o programa te retornara sua raiz quadrada\nDigite um Numero:'))

if numero1 >= 0:
    raiz = numero1 ** 0.5
    print(f'A raiz quadrada de {numero1} é {raiz}')
else:
    print(f'numero invalido')
