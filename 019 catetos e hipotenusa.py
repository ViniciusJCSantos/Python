from math import hypot
oposto = float(input('Digite o cumprimento do cateto oposto: '))
adjacente = float(input('Digite o cumprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('A hipotenusa é {:.2f}.'.format(hipotenusa))