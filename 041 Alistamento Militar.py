ano = int(input('Digite seu ano de nascimento: '))
from time import sleep
print('Analisando...')
sleep(3)
from datetime import date
hoje = date.today().year
idade = hoje - ano
if idade == 18:
    print('Você precisa se alistar esse ano.')
elif idade > 18:
    saldo = idade - 18
    print('Você devia ter se alistado há {} anos.'.format(saldo))
    alist = hoje - saldo
    print('Seu ano de alistamento foi {}.'.format(alist))
else:
    saldo = 18 - idade
    print('Você deve se alistar em {} anos.'.format(saldo))
    alist = hoje + saldo
    print('O ano de seu alistamento será {}.'.format(alist))
