nome = str(input('Digite o seu nome completo: ')).strip()
print("""Analisando seu nome...
Seu nome em letras maiúsculas: {}
Seu nome em letras minúsculas: {}""".format(nome.upper(), nome.lower()))
print('Seu nome completo tem {} letras.'.format(len(nome) - nome.count(' ')))
nome2 = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(nome2[0], len(nome2[0])))
