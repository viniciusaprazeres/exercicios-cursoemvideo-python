sexo = input('Informe seu sexo: [M/F] ')

while sexo not in 'mMfF':
    sexo = input('Dados inválidos. Por favor, informa seu sexo: ')

print(f'Sexo {sexo} registrado com sucesso.')
