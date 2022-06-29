cont = 0
n = 0
s = 0
while n != 999:
    n = int(input('Digite um número ou digite 999 para sair: '))
    cont += 1
    s += n
    if n == 999:
        cont -= 1
        s -= n
print('Foram digitado {} números e a soma deles é {}.'.format(cont, s))