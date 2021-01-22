"""

"""
qtd = int(input('Quantos numeros voce quer?'))
maior = 0
contador = 1

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor : '))
    if num > maior:
        maior = num
    elif maior == num:
        contador += 1
print(f'O maior numero é {maior} e ele aparece {contador} vezes')
