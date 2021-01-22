"""
soma dos 50 primeiros numeros pares
"""
soma = 0
for n in range(0, 51, 2):
    print(n)
    soma = soma + n

print(f'A soma é {soma}')
