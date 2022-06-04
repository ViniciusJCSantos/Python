n = int(input('Digite um número: '))
d = 0
for primo in range(1, n+1):
    if(n % primo == 0):
        d += 1
if(d == 2):
    print('Esse número é primo')
else:
    print('Esse número não é primo')
