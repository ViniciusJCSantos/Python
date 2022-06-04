from random import choice
from time import sleep
print('\33[34m-=\33[m'*20)
print('\33[35m {: ^40} \33[m'. format('JOKENPÔ!!!'))
print('\33[34m-=\33[m'*20)
jogador = str(input('Escolha pedra, papel ou tesoura: ')).strip()
pd = 'pedra'
pp = 'papel'
ts = 'tesoura'
lista = [pd, pp, ts]
computador = choice(lista)
print('*'*40)
if jogador == 'pedra' and computador == 'tesoura' or jogador == 'tesoura' and computador == 'papel' or jogador == 'papel' and computador == 'pedra':
    print('\033[34m {: ^20}\033[m'.format(' JO... '))
    sleep(1)
    print('\033[34m {: ^30}\033[m'.format(' KEN...'))
    sleep(1)
    print('\033[34m {: ^43}\033[m'.format(' POOO!!!!'))
    print('Jogador: {}\nComputador: {}\n\033[34m PARABÉNS!!! CONSEGUIU ME VENCER!!!\033[m'.format(jogador, computador))
elif jogador == 'tesoura' and computador =='pedra' or jogador == 'papel' and computador == 'tesoura' or jogador == 'pedra' and computador == 'papel':
    print('\033[34m {: ^20}\033[m'.format(' JO... '))
    sleep(1)
    print('\033[34m {: ^30}\033[m'.format(' KEN...'))
    sleep(1)
    print('\033[34m {: ^43}\033[m'.format(' POOO!!!!'))
    print('Jogador: {}\nComputador: {}\n\033[33mVocê perdeu!!!! HAHAHAHAHA!!!!\033[m'.format(jogador, computador))
elif jogador == computador:
    print('\033[34m {: ^20}\033[m'.format(' JO... '))
    sleep(1)
    print('\033[34m {: ^30}\033[m'.format(' KEN...'))
    sleep(1)
    print('\033[34m {: ^43}\033[m'.format(' POOO!!!!'))
    print('Jogador: {}\nComputador: {}\nEMPATE!!! Sorte de principiante!!!'.format(jogador, computador))
else:
    print("""\033[31m {:*^40} \033[m
    \033[34m Escolha PEDRA, PAPEL OU TESOURA...\033[m""". format(' JOGADA INVÁLIDA!!! '))
print('*' * 40)
