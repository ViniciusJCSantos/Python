from math import factorial
print('*'*50)
print('Olá! Vamos calcular fatoriais?')
print('*'*50)
num = int(input('Digite um número: '))
for c in range(num, 0, -1):
    print(c, end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f = factorial(num)
print(f)
print('FIM!')
