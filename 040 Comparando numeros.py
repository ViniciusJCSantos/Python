from time import sleep
print('Olá, vamos comparar a grandeza dos números?')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print('ANALISANDO...')
sleep(3)
if num1 > num2:
    print('Os números digitados foram {} e {} e o primeiro número é maior que o segundo'.format(num1, num2))
elif num2 > num1:
    print('Os números digitados foram {} e {} e o segundo número é maior que o primeiro'.format(num1, num2))
else:
    print('Os números digitados são iguais.')
