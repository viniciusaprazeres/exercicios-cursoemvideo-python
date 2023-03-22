maiores_de_idade = 0
homens = 0
mulheres_menores_de_vinte = 0

while True:
    print(24 * '-')
    print('  CADASTRE UMA PESSOA')
    print(24 * '-')

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: '))

    if idade > 18:
        maiores_de_idade += 1

    if sexo in 'Mm':
        homens += 1

    if sexo in 'Ff' and idade < 20:
        mulheres_menores_de_vinte += 1

    print(24 * '-')
    continuar = input('Quer continuar? [S/N] ')

    while continuar not in 'SsNn':
        continuar = input('Quer continuar? [S/N] ')

    if continuar in 'Nn':
        print(24 * '-')
        break

print(f'\nTotal de pessoas com mais de 18 anos de idade: {maiores_de_idade}.')
print(f'Total de homens cadastrados: {homens}.')
print(f'Total de mulheres com menos de 20 anos de idade:  {mulheres_menores_de_vinte}.')
