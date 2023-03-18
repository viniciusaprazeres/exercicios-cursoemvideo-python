print(f'Gerador de PA')
print(10 * '-=')

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = primeiro_termo
contador = 1
pausa = 10
numero_de_termos = 0

while contador <= pausa:
    print(f'{termos} → ', end='')
    termos += razao
    contador += 1
    numero_de_termos += 1

    if contador > pausa:
        contador = 1
        pausa = int(input('PAUSA \nQuantos termos a mais você deseja mostrar? '))

        if pausa == 0:
            print(f'Progressão finalizada com {numero_de_termos} termos mostrados.')
