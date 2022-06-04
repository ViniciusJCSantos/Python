p = int(input('Qual a distância da viagem? '))
print('Você está prestes a iniciar uma viagem de {} KM.'.format(p))
if p <= 200:
    print('Sua passagem vai custar R${}.'.format(p*0.5))
else:
    print('Sua passagem vai custar R${}.'.format(p*0.45))

print('='*12, 'BOA VIAGEM!!!', '='*12)
