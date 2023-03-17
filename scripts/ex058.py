import random

numero = random.randint(0, 10)
print(numero)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

tentativas = 0
acertou = False

while not acertou:
    tentativas += 1
    palpite = int(input('Qual é seu palpite? '))
    if palpite < 0 or palpite > 10:
        print('Por favor digite um número entre 0 e 10.')
    elif palpite < numero:
        print('Mais... Tente mais uma vez!')
    elif palpite > numero:
        print('Menos... Tente mais uma vez!')
    else:
        acertou = True

if tentativas == 1:
    print('Acertou com 1 tentativa. Parabéns!')
else:
    print(f'Acertou com {tentativas} tentativas. Parabéns!')
