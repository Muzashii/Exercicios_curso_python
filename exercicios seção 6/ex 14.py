"""
numeros naturais ate o numeor escolhido decrecente par
"""
numero = int(input(f'Digite um numero: '))
if(numero%2) == 0 :
    for num in range(numero, -1, -2):
        print(num)
else:
    numero -= 1
    for num in range(numero, -1, -2):
        print(num)