print('='*40)
print('        CALCULADORA DE \33[32mI.M.C.\33[m')
print('='*40)
peso = float(input('Digite seu peso em quilos: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura**2)
print('Seu I.M.C. é {:.2f}.'.format(imc))
if imc < 18.5:
    print('ATENÇÂO!!! Você está ABAIXO DO PESO.')
elif imc <= 25:
    print('PARABÉNS!!! Você está no PESO IDEAL.')
elif imc <= 30:
    print('ATENÇÃO!!! Você está com SOBREPESO.')
elif imc <= 40:
    print('CUIDADO!!! Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA. Procure ajuda de um profissional.')
