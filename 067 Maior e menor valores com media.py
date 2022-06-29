r = 'S'
cont = s = md = maior = menor = 0
while r == 'S':
    n = int(input('Digite um número: '))
    cont += 1
    s += n
    r = str(input('Deseja continuar?[S/N] ')).strip().upper()
    while r not in 'SN' or r == '':
        print('Resposta inválida.')
        r = str(input('Deseja continuar?[S/N} ')).strip().upper()
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > cont:
            n = maior
        if n < menor:
            menor = n
md = s / cont
print("""Foram digitado {} valores e a média deles é {}.
Sendo {} o menor valor e {} o maior valor.""".format(cont, md, menor, maior))
