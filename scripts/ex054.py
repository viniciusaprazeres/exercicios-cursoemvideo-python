import datetime

anos_nascimentos = []
ano_atual = datetime.datetime.now().year
menores = maiores = 0

for i in range(0, 7):
    anos_nascimentos.append(int(input(f"Em que ano a {i + 1} pessoa nasceu?: ")))
    idade = ano_atual - anos_nascimentos[i]
    if idade < 18:
        menores += 1
    elif idade >= 18:
        maiores += 1
    else:
        print('Erro! Digite um ano válido.')

print(f'Ao todo há {maiores} pessoas maiores de idade.')
print(f'Já o número de pessoas menores de idade é igual a {menores}.')
