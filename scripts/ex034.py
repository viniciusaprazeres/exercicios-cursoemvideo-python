salario_inicial = float(input('Digite o salário do funcionário R$: '))

if salario_inicial > 1250:
    salario_final = salario_inicial + (0.1 * salario_inicial)
elif salario_inicial <= 1250:
    salario_final = salario_inicial + (0.15 * salario_inicial)
else:
    print('ERRO! Digite um número válido.')

print(f'O funcionário que ganha R$ {salario_inicial:.2f} passará a ganhar R$ {salario_final:.2f}')