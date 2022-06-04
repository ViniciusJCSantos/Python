nome = str(input('Digite o nome do colaborador: ')).strip().title()
s = float(input('Digite o salário do colaborador: R$ '))
if s > 1250:
    print('O salário do colaborador {} será de R${:.2f}.'.format(nome, (s*0.1 + s)))
else:
    print('O salário do colaborador {} será de R${:.2f}.'.format(nome, (s*0.15 + s)))
print('='*12, 'FIM', '='*12)
