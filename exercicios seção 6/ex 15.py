"""
numeros naturais ate o numeor escolhido crescente impar
"""
numero = int(input(f'Digite um numero: '))
if(numero%2) == 0 :
    numero -= 1
    for num in range(1, numero+1, 2):
        print(num)
else:
    for num in range(1, numero+1, 2):
        print(num)