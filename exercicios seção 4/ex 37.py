"""
desconto de 12%
"""

preço = float(input(f'Digite o vaor do produto que deseja receber o desconto de 12%\nPreço do produto: '))

descon = preço * 0.12
final = preço - descon

print(f'Seu produto de R${preço} recebeu um desconto de R${descon} e agora seu preço é R${final}')
