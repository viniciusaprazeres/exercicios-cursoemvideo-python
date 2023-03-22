total = 0
mais_de_mil = 0
nome_mais_barato = 0
preco_mais_barato = 0
primeiro_preco = True

print(25 * '-')
print('  LOJA SUPER BARATÃO')
print(25 * '-')


while True:
    nome_do_produto = str(input('Nome do produto: '))
    preco = float(input('Preço R$: '))

    total += preco

    if preco > 1000:
        mais_de_mil += 1

    if primeiro_preco or preco < preco_mais_barato:
        preco_mais_barato = preco
        nome_mais_barato = nome_do_produto
        primeiro_preco = False

    print(25 * '-')
    continuar = input('Quer continuar? [S/N] ')
    print(25 * '-')

    while continuar not in 'SsNn':
        continuar = input('Quer continuar? [S/N] ')

    if continuar in 'Nn':
        break


print('\n' + 4 * '-' + ' FIM DO PROGRAMA ' + 4 * '-' )
print(f'\nO total da compra foi R$: {total:.2f}')
print(f'Há {mais_de_mil} produto custando mais de mil reais.')
print(f'O produto mais barato foi {nome_mais_barato} custando R$: {preco_mais_barato:.2f}')
