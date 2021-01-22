"""
calculadora de 10 numeros
"""
soma = 0
conta = 1
for n in range(1, 11):
    num = float(input(f'Informe o {conta} numero da soma: '))
    conta += 1
    soma += num
print(f'A soma é {soma}')
