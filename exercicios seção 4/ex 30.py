"""
cotação do dolar
"""

real = float(input(f'Escreva um valor em real e a cotaçao do dolar para receber a conversão:\nvalor em Real $: '))
cotação = float(input(f'Escreva o valor da Cotação do dolar atual: '))

total = real / cotação

print(f'Com R${real} e cotação de ${cotação} da um total de ${total} dolares ')