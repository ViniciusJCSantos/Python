preço = float(input('Digite o preço do produto (use ponto): R$ '))
promoção = preço - (preço * 0.05)
# promoção = preço - (preço * 5 / 100)
print('O preço do produto é de R$ {:.2f}, mas após o desconto, será de R$ {:.2f}.'.format(preço, promoção))
