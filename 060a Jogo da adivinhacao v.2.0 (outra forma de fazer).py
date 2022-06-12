from random import randint
num = randint(0, 10)
print('*' * 30)
print('Olá!\nSou seu computador.\nNesse momento estou pensando em número de  0 a  10.\nConsegue adivinhar qual é?')
print('*' * 30)
acertou = False
tentativa = 0
while not acertou:
    r = int(input('Que número estou pensando? '))
    tentativa += 1
    if r == num:
        acertou = True
    else:
        if r > num:
            print('Tente outra vez. Que tal um número menor?')
        elif r < num:
            print('Tente outra vez. Acho que é um número maior!')
print('Você acertou após {} tentativa(s). O número que eu estava pensando era {}.'.format(tentativa, num))
