print('\33[33m*\33[m'*40)
print('    \33[34mANALISADOR DE TRIÂNGULOS 2.0.\33[m')
print('\33[33m*\33[m'*40)
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1 < r2 + r3 or r2 < r1 + r3 or r3 < r1 + r2:
    print('Essas retas PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Essa retas NÃO PODEM formar um triângulo.')
