"""
menu com opiçoes
"""
escolha = int(input(f'Escolha a opção:\n1-Soma de 2 números.\n2-Diferença entre 2 numeros(maior pelo menor)'
                          f'\n3-Produto entre 2 numeros\n4-divisão entre 2 numeros(o denominador nao pode ser zero)'
                    f'\nOpição:'))
numeroum = float(input(f'Digite o primeiro numero:'))
numerodois = float(input(f'Digite o segundo numero:'))

if escolha == 1:
    soma = numeroum + numerodois
    print(f'A soma de {numeroum} + {numerodois} = {soma}')
elif escolha == 2:
    if numeroum > numerodois:
        numeum = numeroum - numerodois
        print(f'A diferença entre {numeroum} e {numerodois} é igual a {numeum}')
    else:
        numedois = numerodois - numeroum
        print(f'A diferença entre {numerodois} e {numeroum} é igual a {numedois}')
elif escolha == 3:
    prod = numeroum * numerodois
    print(f'O produto é {prod}')
elif escolha == 4:
    divi = numeroum / numerodois
    print(f'A divisao da {divi}')
else:
    print(f'Erro')