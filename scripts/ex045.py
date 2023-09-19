import random
from time import sleep

print('Você tem 3 opções: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
opcao_jogador = int(input('Qual a sua escolha?: '))
opcao_computador = random.randint(0, 2)

if opcao_jogador < 0 or opcao_jogador > 2:
    print('ERRO! Escolha uma opção válida.')
    exit()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print(30 * '=')
print(f'O computador jogou {opcoes[opcao_computador]}')
print(f'O jogador jogou {opcoes[opcao_jogador]}')
print(30 * '=')

if opcao_jogador == 0 and opcao_computador == 1:
    print('COMPUTADOR VENCE!')
elif opcao_jogador == 1 and opcao_computador == 0:
    print('JOGADOR VENCE!')
elif opcao_jogador == 1 and opcao_computador == 2:
    print('COMPUTADOR VENCE!')
elif opcao_jogador == 2 and opcao_computador == 1:
    print('JOGADOR VENCE!')
elif opcao_jogador == 2 and opcao_computador == 0:
    print('COMPUTADOR VENCE!')
elif opcao_jogador == 0 and opcao_computador == 2:
    print('JOGADOR VENCE!')
else:
    print('EMPATE')