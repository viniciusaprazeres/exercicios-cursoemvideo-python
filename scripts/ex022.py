nome = input('Digite seu nome completo: ')
nome_separado = nome.split()
tamanho = len(''.join(nome_separado))

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome.lower()}.')
print(f'Seu nome tem ao todo {tamanho} letras.')
print(f'Seu primeiro nome é {nome_separado[0]} e ele tem {len(nome_separado[0])} letras.')
