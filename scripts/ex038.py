primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

if primeiro_numero > segundo_numero:
    print('O PRIMEIRO valor é MAIOR que o segundo!')
elif primeiro_numero < segundo_numero:
    print('O SEGUNDO valor é MAIOR que o primeiro!')
else:
    print('Os DOIS valores são IGUAIS!')