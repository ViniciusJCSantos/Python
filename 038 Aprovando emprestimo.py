imóvel = float(input('Informe o valor do imóvel: R$ '))
renda = float(input('Informe a sua renda: R$ '))
tempo = int(input('Informe em quantos anos você vai pagar: '))
prestação = imóvel / (tempo * 12)
limite = renda * 30 / 100
if prestação <= limite:
    print('Seu empréstimo foi aprovado!')
else:
    print('Seu empréstimo foi negado, pois ultrapassa o limite de 30% de sua renda.')
print('O valor do imóvel é R${:.2f}, dividido em {} parcelas de R${:.2f}.'.format(imóvel, tempo, prestação))
