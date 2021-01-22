"""
calculadora de media de 10 numeros
"""
soma = 0
conta = 1
for n in range(1, 11):
    num = float(input(f'Informe o {conta} numero da soma para a media: '))
    conta += 1
    soma += num

media = soma / 10

print(f'A media é {media}')
