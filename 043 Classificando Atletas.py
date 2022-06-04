from datetime import date
idade = int(input('Digite o ano de nascimento do atleta: '))
hoje = date.today().year
classe = hoje - idade
print('O atleta tem {} anos.'.format(classe))
if classe <= 9:
    print('Categoria: MIRIM.')
elif classe <= 14:
    print('Categoria: INFANTIL.')
elif classe <= 19:
    print('Categoria: JUNIOR.')
elif classe <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER.')
print('*'*20, '\33[34mBONS JOGOS!!!\33[m', '*'*20)
