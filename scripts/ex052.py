numero = int(input('Digite um número: '))
quantidade = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[1;92m', end=' ')
        quantidade += 1
    elif numero % i != 0:
        print('\033[1;91m', end=' ')

    print(f'{i}', end=' ')

print(f'\n\033[mO número {numero} foi divisível {quantidade} vezes.')
print('E por isso ele NÃO É PRIMO!' if quantidade != 2 else 'E por isso ELE É PRIMO!')
