nomes = []
idades = []
sexos = []

for i in range(0, 4):
    print(7 * '-' + f' Pessoa {i + 1} ' + 7 * '-')
    nomes.append(str(input('Nome: ')))
    idades.append(int(input('Idade: ')))
    sexos.append(str(input('Sexo [M/F]: ')))

media = sum(idades) / 4
idade_maxima = max(idades)
indice_idade_maxima = idades.index(idade_maxima)
mulheres_menos_vinte = 0

for j in range(0, 4):
    if idades[j] < 20 and sexos[j] in 'fF':
        mulheres_menos_vinte += 1

print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {idade_maxima} anos e se chama {nomes[indice_idade_maxima]}.')
print(f'Ao todo são {mulheres_menos_vinte} mulher(es) com menos de 20 anos.')
