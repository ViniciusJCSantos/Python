real = float(input('Quanto dinheiro você tem (use ponto)? R$ '))
dólar = real / 3.27
print('Com R${} você pode comprar US${:.2f} na data de hoje.'.format(real, dólar))
