f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
inv = ''
for c in range(len(j) - 1, -1, -1):
    inv += j[c]
if j == inv:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')
