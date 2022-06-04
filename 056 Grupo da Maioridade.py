from datetime import date
hoje = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = hoje - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Um total de {} pessoas é maior.'.format(maior))
print('Um total de {} pessoas é menor.'.format(menor))
