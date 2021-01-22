"""
pode ou nao se aposentar
"""
print(f'Escreva sua idade e seu tempo em anos de serviço, que te falarei se pode ou nao se aposentar')
idade = int(input(f'Digite sua idade:'))
tempo = int(input(f'Digite seu tempo de serviço em anos:'))

if idade >= 65 or tempo >= 30 or idade >= 60 and tempo >= 25:
    print(f'Voce pode se aposentar')
else:
    print(f'Voce nao pode se aposentar ainda')