alt = float(input('Digite a altura da parede (use ponto): '))
lar = float(input('Digite a largura da parede (use ponto): '))
área = alt * lar
tinta = área / 2
print('A parede tem a altura de {} metros e a largura de {} metros, com uma área de {:.2f} m².\nPara pintar essa parede são necessários {:.2f} litros de tinta.'.format(alt, lar, área, tinta))
