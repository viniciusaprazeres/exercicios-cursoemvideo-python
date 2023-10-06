listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32,
            'Canetas', 22.30, 'Livro', 34.90)



print(40 * '-')
print(10 * ' ' + 'LISTAGEM DE PREÇOS')
print(40 * '-')

for i in range(0, 18):
    if i % 2 == 0: print(f'{listagem[i]:.<30}', end='')
    else: print(f'R$ {listagem[i]:>6.2f}')

print(40 * '-')
