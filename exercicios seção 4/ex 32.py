"""
soma do sucessor do triplo com o antecessor de seu dobro
"""
numero = int(input(f'Digite um numero que te mostrarei soma do sucessor do triplo com o antecessor de seu dobro:'
                   f'\nDigite um numero:'))
tri = (numero * 3) + 1
ant = (numero * 2) - 1

total = tri + ant

print(f'Voce escolheu o numero {numero}, o antecessor de seu dobro é {ant} e sucessor do triplo é {tri}, e a soma dos '
      f'dois é igual a {total}')
