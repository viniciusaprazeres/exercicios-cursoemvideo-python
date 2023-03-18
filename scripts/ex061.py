print(f'Gerador de PA')
print(10 * '-=')

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = primeiro_termo
contador = 1

while contador <= 10:
    print(f'{termos} → ', end='')
    termos += razao
    contador += 1

print('FIM!')
