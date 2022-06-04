print('='*30)
print('ANALISADOR DE TRIÂNGULOS')
print('='*30)
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 or r2 < r1 + r3 or r3 < r1 + r2:
    print('Essas retas PODEM FORMAR um triângulo.')
else:
    print('Essa retas NÃO PODEM formar um triângulo.')
print('='*12, 'FIM', '='*12)
