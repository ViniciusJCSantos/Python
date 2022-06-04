num = int(input('Digite um número: '))
print('Certo. Posso converter esse número para:\n[1] binário;\n[2] octal;\n[3] hexadecimal.')
import numbers
bin = bin(num)
oct = oct(num)
hexa = hex(num)
conv = int(input('Digite a opção desejada: '))
if conv == 1:
      print('O número escolhido foi {} e convertido para binário fica {}.'.format(num, bin[2:]))
elif conv == 2:
      print('O número escolhido foi {} e convertido para octal fica {}.'.format(num, oct[2:]))
elif conv == 3:
      print('O número escolhido foi {} e convertido para hexadecimal fica {}.'.format(num, hexa[2:]))
else:
      print('Opção inválida. Escolhas uma das opções listadas acima.')
