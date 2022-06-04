from time import sleep
import emoji
print('{:*^50}'.format('CONTAGEM REGRESSIVA'))
print('...')
sleep(3)
for time in range(10,  0, -1):
    print(time)
    sleep(1)
print()
print(emoji.emojize('{::fireworks:^50}').format('FELIZ ANO NOVO!!!'))
