sexo = str(input('Digite o seu sexo [M/F]: ')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('Resposta inválida! Por favor, digite seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} incluído com sucesso.'.format(sexo))
