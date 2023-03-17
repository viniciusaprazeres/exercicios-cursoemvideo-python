primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
menu = 0

while menu != 5:
    print('     [ 1 ] Somar')
    print('     [ 2 ] Multiplicar')
    print('     [ 3 ] Maior')
    print('     [ 4 ] Novos números')
    print('     [ 5 ] Sair do programa')
    menu = int(input('>>>>>> Qual é sua opção? '))

    if menu == 1:
        print(f'A soma de {primeiro} + {segundo} é {primeiro + segundo}')
        print(30 * '=')
    elif menu == 2:
        print(f'A multiplicação entre {primeiro} e {segundo} é {primeiro * segundo}')
        print(30 * '=')
    elif menu == 3:
        if primeiro > segundo:
            print(f'Entre os números {primeiro} e {segundo} o maior é {primeiro}.')
            print(30 * '=')
        elif primeiro < segundo:
            print(f'Entre os números {primeiro} e {segundo} o maior é {segundo}.')
            print(30 * '=')
        else:
            print('Os dois números são iguais!')
            print(30 * '=')
    elif menu == 4:
        print('Informa os números novamente.')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    elif menu < 1 or menu > 5:
        print('Opção inválida. Tente novamente.')

print('Finalizando...')
print(30 * '=')
print('Fim do programa. Volte sempre!')