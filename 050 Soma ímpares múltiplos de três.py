s = 0
for c in range(1, 500):
    if (c % 3) == 0:
        if (c % 2) == 1:
            s += c
print('O somatório dos números ímpares, múltiplos de 3, contidos entre 1 e 500 é {}.'.format(s))
