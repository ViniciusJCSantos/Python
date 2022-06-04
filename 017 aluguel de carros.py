dias = int(input('Quantos dias? '))
km = float(input('Quantos Kilômetros rodados? '))
aluguel = (dias * 60) + (km * 0.15)
print('O carro foi alugado por {} dias e rodou {} kilômetros.\nO valor do aluguel é de R$ {:.2f}'.format(dias, km, aluguel))
