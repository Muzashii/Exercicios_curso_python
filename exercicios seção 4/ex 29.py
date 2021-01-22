"""
media de quatro notas
"""
numero1 = float(input(f'Escreva as quatro notas para receber a media aritimetica:\nPrimeira nota: '))
numero2 = float(input(f'Segunda nota: '))
numero3 = float(input(f'Terceira nota: '))
numero4 = float(input(f'Quarta nota: '))

total = (numero1 + numero2 + numero3 + numero4) / 4

print(f'A media das notas {numero1}, {numero2}, {numero3}, {numero4} é igual a {total} ')
