totidades = 0
média = 0
idadehomem = 0
masc = 0
nomevelho = ''
mulher20 = 0
for c in range(1, 5):
    print('====={}ª PESSOA====='.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    totidades += idade
    if c == 1 and sexo in 'Mm':
        masc += 1
        idadehomem = idade
        nomehomem = nome
    if sexo in 'Mm' and idade > idadehomem:
        masc += 1
        idadehomem = idade
        nomehomem = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
média = totidades / 4
print('A média de idade dos participantes é {} anos.'.format(média))
if masc == 0:
    print('Não há homens nesse grupo.')
else:
    print('O homem mais velho se chama {} e tem {} anos.'.format(nomehomem, idadehomem))
print('Temos o total de {} mulheres com menos de 20 anos.'.format(mulher20))
