"""
ignorando negativos
"""
divi = 10
soma = 0
conta = 1
for n in range(1, 11):
    num = float(input(f'Informe o {conta} numero da soma para a media: '))
    conta += 1
    if num >= 0:
        soma += num
    else:
        num = 0
        divi -= 1

media = soma / divi

print(f'A media é {media}')
