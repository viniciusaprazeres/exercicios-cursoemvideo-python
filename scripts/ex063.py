print(22*'=')
print('Sequência de Fibonacci')
print(22*'=')

numero = int(input('Digite o número de termos da sequência Fibonacci que deseja saber: '))
contador = 1
primeiro_termo = 0
segundo_termo = 1
terceiro_termo = 1


while contador <= numero:
    if contador == 1:
        print(f'{primeiro_termo} → ', end='')
    elif contador == 2:
        print(f'{segundo_termo} → ', end='')
    else:
        print(f'{terceiro_termo} → ', end='')
        primeiro_termo = segundo_termo
        segundo_termo = terceiro_termo
        terceiro_termo = primeiro_termo + segundo_termo

    contador += 1
print('FIM!')