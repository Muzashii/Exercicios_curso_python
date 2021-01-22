"""
calculadora basica
"""
escolha = int(input(f'Escolha uma das opições: \n1-soma\n2-subtração\n3-divisão\n4-multiplicação\nopção escolida: '))
numro1 = float(input(f'Digite o primeiro valor:'))
numro2 = float(input(f'Digite o segundo valor:'))

if escolha == 1:
    soma = numro1 + numro2
    print(f'{numro1} + {numro2} = {soma}')
elif escolha == 2:
    sub = numro1 - numro2
    print(f'{numro1} - {numro2} = {sub}')
elif escolha == 3:
    div = numro1 / numro2
    print(f'{numro1} / {numro2} = {div}')
elif escolha == 4:
    mul = numro1 * numro2
    print(f'{numro1} * {numro2} = {mul}')
else:
    print(f'Erro')
