"""
ganhadores de um concurso
"""
no1 = str(input(f'Digite o nome dos tres ganhadores do concurso em ordem, do primeiro ao terceiro\nNome do primeiro: '))
no2 = str(input(f'Nome do segundo: '))
no3 = str(input(f'Nome do terceiro: '))

pre = 780_000

# conta do primeiro lugar
prime = pre * 0.46

# conta do segundo lugar
segun = pre * 0.32

# conta do terceiro lugar
ter = pre - (segun + prime)

print(f'O primeiro lugar {no1} ganhara R${prime}, o segundo {no2} ganhara R${segun} e o terceiro {no3} '
      f'recebera R${ter}')
