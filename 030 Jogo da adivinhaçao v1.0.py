from random import randint
from time import sleep
num = randint(0, 5)
print('*'*30)
print('OLá!\nVou pensar em um número de 0 a 5...\nTENTE ADIVINHAR...')
print('*'*30)
n = int(input('Em que número estou pensando? '))
print('PROCESSANDO...')
sleep(3)
print('Estava pensando no número {}.'.format(num))
if n == num:
    print('VOCÊ ME VENCEU...')
    sleep(3)
    print('SORTE DE PRINCIPIANTE...:(')
else:
    print('HA HA HA!!! GANHEI!!!')
    sleep(3)
    print('Vai ter que fazer melhor se quiser me vencer...')
print('='*12)
sleep(3)
print('E aí? Vamos de novo? Ou tá com medo?')