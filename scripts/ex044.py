print(10*'=' + ' LOJA PYTHON' + 10*'=')

preco_inicial = float(input('Digite o preço total das compras: '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista usando dinheiro ou cheque')
print('[ 2 ] à vista usando cartão de crédito (sem juros)')
print('[ 3 ] 2x usando cartão de crédito')
print('[ 4 ] 3x ou mais usando cartão de crédito')
opcao = int(input('Qual é a opção desejada?: '))

if opcao == 1:
    preco_final = preco_inicial - (0.1 * preco_inicial)
elif opcao == 2:
    preco_final = preco_inicial - (0.05 * preco_inicial)
elif opcao == 3:
    preco_final = preco_inicial
    preco_parcelas = preco_final / 2
    print(f'Sua compra será parcelada em 2x de R$ {preco_parcelas:.2f}, SEM JUROS.')
elif opcao == 4:
    preco_final = preco_inicial + (0.2 * preco_inicial)
    quantidade_parcelas = int(input('Em quantas parcelas?: '))
    preco_parcelas = preco_final / quantidade_parcelas
    print(f'Sua compra será parcelada em {quantidade_parcelas}x de R$ {preco_parcelas:.2f}, COM JUROS')
else:
    print('ERRO! Digite uma opção válida!')
    preco_inicial = preco_final = 0

print(f'Sua compra de R$ {preco_inicial:.2f} vai custar R$ {preco_final:.2f} no total.')
