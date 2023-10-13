valores = []
continuar_um = continuar_dois = True

while continuar_um:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')

    while continuar_dois:
        resposta = input('Quer continuar?[S/N] ')

        if 'n' in resposta or 'N' in resposta:
            continuar_um = False
            break
        elif 's' in resposta or 'S' in resposta:
            continuar_um = True
            break
        else:
            print('Por favor, digite uma resposta válida [S/N]')


print(30 * '-=')
print(f'Você adicionou os valores: {sorted(valores)}')
