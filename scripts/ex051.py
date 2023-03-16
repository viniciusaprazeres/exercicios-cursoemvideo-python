primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

for i in range(primeiro_termo, primeiro_termo + 10 * razao, razao):
    print(f'{i} →', end=' ')

print('Acabou!')
