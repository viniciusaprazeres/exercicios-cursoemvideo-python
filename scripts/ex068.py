import random

print(8 * '=-=')
print('VAMOS JOGAR PAR OU ÍMPAR')


valor = 0
computador = 0
total = 0
contador = 0
par_ou_impar = ''
perdeu = False

while perdeu == False:
    print(8 * '=-=')
    valor = int(input('Digite um valor: '))
    par_ou_impar = input('Escolhe Par ou Ímpar? [P/I]: ')

    if par_ou_impar in 'PpIi':
        computador = random.randrange(0, 11)
        total = valor + computador

        if total % 2 == 0 and par_ou_impar in 'Pp':
            perdeu = False
            contador += 1
        elif total % 2 != 0 and par_ou_impar in 'Ii':
            perdeu = False
            contador += 1
        else:
            perdeu = True

        print(30 * '-')
        print(f'Você jogou {valor} e o computador jogou {computador}. Total de {total}: ', end='')
        print('Deu PAR.' if total % 2 == 0 else 'Deu ÍMPAR.')
        print(30 * '-')

        if perdeu == False:
            print('VOCÊ VENCEU! \nVamos jogar novamente...')
            continue
        else:
            print('VOCÊ PERDEU!')
            break

print(f'GAME OVER! Você venceu {contador} vez.')
