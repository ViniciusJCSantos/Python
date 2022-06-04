salário = float(input('Digite o valor do salário (use ponto): R$ '))
reajuste = salário + (salário * 0.15)
# reajuste = salário + (salário * 15 / 100)
print('O colaborador que recebe R$ {:.2f}, passará a receber R$ {:.2f} após o reajuste de 15%.'.format(salário, reajuste))
