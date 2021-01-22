"""
soma dos quadrados de tres numeros
"""
numero1 = float(input(f'Escreva tres numeros para receber a soma de seus quadrados:\nPrimeiro numero: '))
numero2 = float(input(f'Segundo numero: '))
numero3 = float(input(f'Terceiro numero: '))

total = (numero1 ** 2) + (numero2 ** 2) + (numero3 ** 2)

print(f'A soma dos quadrados dos numeros {numero1}, {numero2} e {numero3} é igual a {total} ')