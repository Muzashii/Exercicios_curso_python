"""
programa para ajudar um vendedor
"""
valor = float(input(f'Digite o valor do produto desejado:\nValor do produto: R$'))

# desconto
des = valor * 0.01
valordes = valor - des

# parcela
parcela = valor / 3

# comissao caso a venda seja a vista

vista = valordes * 0.05

# comissao casa a venda seja parcelada

coparce = valor * 0.05

print(f'Com o valor de R${valor}, é possivel fazer isso:')
print(f'- O valor do produto com 10% de desconto é R${valordes}')
print(f'- O valor de cada parcela dividida em 3x é R${parcela}')
print(f'- O valor da comissao em uma venda a vista é R${vista}')
print(f'- O valor da comissao em uma venda parcelada é R${coparce}')
