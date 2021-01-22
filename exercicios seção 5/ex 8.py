"""
mostrar notas validas e a media
"""

nota1 = float(input(f'Digite duas notas validas e recebera sua media\nPrimeira Nota:'))
nota2 = float(input(f'Segunda Nota:'))


if nota1 > 10 or nota2 > 10:
    print(f'Notas invalidas')
elif nota1 < 0 or nota2 < 0:
    print(f'Notas invalidas')
else:
    media = (nota1 + nota2) / 2
    print(f'A media das notas {nota1} e {nota2} é igual a {media} ')
