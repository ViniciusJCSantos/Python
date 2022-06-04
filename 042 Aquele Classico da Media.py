n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
md = (n1 + n2) / 2
print('Você teve as notas {} e {}, sua média é {}.'.format(n1, n2, md))
if md >= 7:
    print('Você foi \33[34mAPROVADO.\33[m Parabéns!')
elif md >= 5 <= 6.9:
    print('Você precisará fazer as aulas de \33[33mRECUPERAÇÃO.\33[m')
else:
    print('Você foi \33[31mREPROVADO.\33[m')