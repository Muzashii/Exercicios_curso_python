"""
raiz e quadrado de numero possitivo
"""

numero = int(input(f'Digite um numeros, caso seja possitivo o programa te retornara ele ao quadrado e sua raiz '
                   f'\nDigite um Numero:'))

if numero >= 0:
    raiz = numero ** 0.5
    print(f'A raiz quadrada de {numero} é {raiz}')
    quadra = numero ** 2
    print(f'O quadrado do numero {numero} é {quadra}')
else:
    print(f'numero invalido')
