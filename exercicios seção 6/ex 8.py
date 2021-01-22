"""
maior e menor numeros
"""
"""
ignorando negativos
"""
conta = 1
soma = 0
menor = 1000000
for n in range(1, 11):
    num = int(input(f'Informe o {conta} numero da soma para a media: '))
    conta += 1
    if num > soma:
        soma = num
    elif num < menor:
        menor = num
print(f'O numero menor é {menor} e o maior é {soma}')
