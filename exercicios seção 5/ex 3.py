"""
numero possitivo ou negativo
"""

numero = int(input(f'Digite um numeros e o programa te retornara sua raiz quadrada caso seja positivo e '
                   f'seu quadrado caso seja negativo\nDigite um Numero:'))

if numero >= 0:
    raiz = numero ** 0.5
    print(f'A raiz quadrada de {numero} é {raiz}')
else:
    quadra = numero ** 2
    print(f'O quadrado do numero {numero} é {quadra}')
