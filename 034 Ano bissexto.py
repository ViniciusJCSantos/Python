#from calendar import isleap
from datetime import date
ano = int(input('Digite o ano. Para o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
#if isleap(ano) == True:
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Analisando o ano de {}...\nVerificamos que ele é BISSEXTO.'.format(ano))
else:
    print('Analisando o ano de {}...\nVerificamos que ele NÃO É BISSEXTO.'.format(ano))

print('='*12, 'FIM', '='*12)
