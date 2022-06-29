from math import factorial
print('-' * 50)
print('Olá! Vamos calcular fatoriais?')
print('-' * 50)
num = int(input('Digite um número: '))
c = num
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    c -= 1
    r = factorial(num)
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
print(r)
print('FIM!')
