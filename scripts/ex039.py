import datetime

ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')

if idade < 18:
    diferenca = 18 - idade
    print(f'Ainda faltam {diferenca} anos para o alistamento militar.')
    print(f'Seu alistamento será em {ano_atual + (diferenca)}.')
elif idade > 18:
    diferenca = idade - 18
    print(f'Você já deveria ter se alistado há {diferenca} anos.')
    print(f'Seu alistamento foi em {ano_atual - diferenca}.')
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
else:
    print('Erro! Digite uma idade válida.')
