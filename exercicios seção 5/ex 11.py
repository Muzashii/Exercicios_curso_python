"""
dividir e somar um numero
"""
numero = int(input(f'Digite um numero para a soma dos algarismos:\nNumero: '))

soma = 0
while(numero > 0):
    soma += numero % 10
    numero = int(numero /10)
print(soma)