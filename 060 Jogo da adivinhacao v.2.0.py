from random import randint
num = randint(0, 10)
print('*' * 30)
print('Olá! \nEstou pensando em número de  0 a  10.\nTente adivinhar qual é.')
print('*' * 30)
r = int(input('Que número estou pensando? '))
t = 1
while r != num:
    t += 1
    if r < num:
        r = int(input('Mais... Tente outra vez: '))
    elif r > num:
        r = int(input('Menos... Tente outra vez: '))
print('Após {} tentativas, você acertou. O número que eu estava pensando era {}.'.format(t, num))