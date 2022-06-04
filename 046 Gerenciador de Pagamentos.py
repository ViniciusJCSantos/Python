print('\033[34m{:*^40}\033[m'.format(' LOJAS EBENÉZER '))
preço = float(input('Digite o valor do produto (use ponto no lugar da vígula): '))
print("""\033[33mFORMAS DE PAGAMENTO:
[1] = À vista no dinheiro ou cheque;
[2] = À vista no cartão;
[3] = Parcelado em 2X no cartão;
[4] = Parcelado em 3X ou mais no cartão.\033[m""")
condição = int(input('\033[34mEscolha a FORMA DE PAGAMENTO de acordo com as opções acima: \033[m'))
if condição == 1:
    total = preço - (preço * 0.10)
    print('O valor total do produto será R${:.2f}.'.format(total))
elif condição == 2:
    total = preço - (preço * 0.05)
    print('O valor total do produto será R$ {:.2f}.'.format(total))
elif condição == 3:
    total = preço
    parcela = preço / 2
    print('O valor total do produto será R$ {:.2f} em 2 parcelas de R$ {:.2f}.'.format(preço, parcela))
elif condição == 4:
    p1 = (int(input('Digite a quantidade de parcelas: ')))
    total = preço + (preço * 0.20)
    p2 = total / p1
    print('O valor total do produto será R$ {:.2f}. Dividido em {} parcelas de R$ {:.2f}.'.format(total, p1, p2))
else:
    print('\033[31m FORMA DE PAGAMENTO INEXISTENTE!!! Escolha uma das opções acima.\033[m')
