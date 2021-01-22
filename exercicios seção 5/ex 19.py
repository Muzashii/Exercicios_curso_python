"""
dividir por 3 ou 5
"""
num = int(input(f'Digite um numero e te falarei se ele é dividido por 3 ou 5: \nNumero:'))

portres = num % 3
porcin = num % 5
print(f'{porcin}, {portres}')

if portres == 1:
    print(f'O numero {num} nao é divisivo por 3')
elif portres == 0:
    print(f'O numero {num} é divisivo por 3')
else:
    print(f'Erro')
if porcin == 1:
    print(f'O numero {num} nao é divisivo por 5')
elif porcin == 0:
    print(f'O numero {num}é divisivo por 5')
else:
    print(f'Erro')
