cont = n = s = 0
n = int(input('Digite um número ou digite 999 para sair: '))
while n != 999:
    cont += 1
    s += n
    n = int(input('Digite um número ou digite 999 para sair: '))
print('Foram digitado {} números e a soma deles é {}.'.format(cont, s))