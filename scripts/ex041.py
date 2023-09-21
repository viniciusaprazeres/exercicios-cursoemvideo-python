import datetime

ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento

print(f'O atleta tem {idade} anos de idade.')

if idade <= 9:
    print('Classificação: MIRIM.')
elif 9 < idade <= 14:
    print('Classificação: INFANTIL.')
elif 14 < idade <= 19:
    print('Classificação: JUNIOR.')
elif 19 < idade <= 25:
    print('Classificação: SÊNIOR.')
elif idade > 25:
    print('Classificação: MASTER.')
else:
    print('Erro! Digite um ano válido.')