"""
contratar ancanador
"""
dias = int(input(f'Digite o numero de dias que o encanador trabalhou (ele recebe R$30,00 por dia):\nNumero de dias: '))

sala = dias * 30
des = sala * 0.08
final = sala - des

print(f'O salario total é R${sala}, com desconto de 8% para o imposto de renda temos R${final} com um total de {dias} '
      f'trabalhados')
