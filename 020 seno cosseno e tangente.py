from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo de {} possui o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}.'.format(ângulo, seno, cosseno, tangente))
