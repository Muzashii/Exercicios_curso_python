"""
calculo da hipotenusa
"""
A = float(input(f'Escreva o valor dos catetos para obter o valor da hipotenusa:\nValor de A: '))
B = float(input('Valor de B: '))

hipo = ((A ** 2) + (B ** 2)) ** 0.5

print(f'Com os catetos {A} e {B}, se tem uma hipotenusa de {hipo}')
