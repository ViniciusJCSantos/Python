vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    print('Você ultrapassou o limite de 80 KM/H e foi MULTADO em R${:.2f}.'.format((vel - 80) * 7))
print('='*12, 'TENHA UM BOM DIA! DIRIJA COM SEGURANÇA!','='*12)
