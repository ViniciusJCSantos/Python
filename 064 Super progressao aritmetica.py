n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
t = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(t), end=' = ')
        t += r
        cont += 1
    print('PAUSA!')
    mais = int(input('Quantos termos gostaria de acrescentar? '))
print('Progressão finalizada com {} termos.'.format(total))
