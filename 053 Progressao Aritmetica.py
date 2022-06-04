n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
e = 10
pa = n + (e - 1) * r
pa += 1
print('Os primeiros 10 termos dessa progressão aritmética são:')
for c in range(n, pa, r):
    print(c,end=' - ')
print('Fim!')
