valor = 0
contador = 1

while True:
    digito = input('Digite o valor da tabuada que deseja ver [Negativo ou Letra para encerrar]: ')
    print(45 * '-')

    if digito.isnumeric():
        valor = int(digito)

        while contador <= 10:
            print(f'{valor} x {contador: <2} = {valor * contador}')
            contador += 1
        print(45 * '-')
        contador = 0
    else:
        break

print('PROGRAMA DE TABUADA ENCERRADO. VOLTE SEMPRE!')
