"""
peso ideal
"""
altura = float(input(f'Digite sua altura e seu peso e te retornaremos seu peso ideal:\n'
                      f'Sua altura: '))
sex = str(input(f'Digite o seu sexo (MASCULINO OU FEMININO): ').upper())

if sex == 'MASCULINO':
    pesoi = (72.7 * altura) - 58
    print(f'Seu peso ideal sendo um homen com {altura} de altura é {pesoi}')
elif sex == 'FEMININO':
    pesoi = (62.1 * altura) - 44.7
    print(f'Seu peso ideal sendo uma mulher com {altura} de altura é {pesoi}')
else:
    print(f'Ocorreu um erro')