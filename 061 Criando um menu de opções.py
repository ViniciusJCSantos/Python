print('Olá.\nVamos testar algumas operações?')
print('=' * 50)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digito o segundo número: '))
op = 0
while op != 5:
    print("""\33[33mTemos as seguintes opções:\n[1] SOMAR\n[2] MULTIPLICAR
[3] SABER QUAL DOS NÚMERO É MAIOR\n[4] ESCOLHER NOVOS NÚMEROS\n[5] SAIR\33[m""")
    op = int(input('Escolha umas das opções [1 a 5]: '))
    if op == 1:
        n3 = n1 + n2
        print('Você escolheu a operação SOMA e o resultado é {}.'.format(n3))
    elif op == 2:
        n3 = n1 * n2
        print('Você escolheu a operação MULTIPLICAÇÃO e o resultado é {}.'.format(n3))
    elif op == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}.'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior que o número {}.'.format(n2, n1))
        else:
            print('Os dois números são iguais.')
    elif op == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        op = 5
    else:
        print('Opção inválida! Tente outra vez')
    print('+'*50)
print('FIM!')
