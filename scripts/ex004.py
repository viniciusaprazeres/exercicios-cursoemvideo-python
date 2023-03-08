algo = input('Digite algo: ')

print('O tipo primitivo desse valor é {}'.format(type(algo)))  #Mostra o tipo primitivo da váriável algo.
print('Só tem espaços? {}'.format(algo.isspace()))  #Verifica se há somente espaços.
print('É um número? {}'.format(algo.isnumeric()))  #Verifica se é um número.
print('É alfabético? {}'.format(algo.isalpha()))  #Verifica se é um caracter alfabético.
print('É alfanumérico? {}'.format(algo.isalnum()))  #Verifica se é um caracter alfanumérico.
print('Está em maiúsculas? {}'.format(algo.isupper()))  #Verifica se está tudo em maiúsculo.
print('Está em minúsculas? {}'.format(algo.islower()))  #Verifica se está tudo em minúsculo.
print('Está capitalizada? {}'.format(algo.istitle()))  #Verifica se a primeira letra está em maiúsculo.
