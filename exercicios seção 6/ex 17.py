"""
calculo dos n primeiros numeros naturais
"""
total = 0
numero = int(input(f'Digite um numero: '))
for num in range(0,numero+1):
    total += num
    print(num)
print(total)