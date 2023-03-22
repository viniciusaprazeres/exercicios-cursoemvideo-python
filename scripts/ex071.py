print(34 * '=')
print(7 * ' ' + 'BANCO CEV')
print(34 * '=')

valor_a_sacar = 0
notas_cinquenta = 0
notas_vinte = 0
notas_dez = 0
notas_um = 0

valor_a_sacar = int(input('Que valor você quer sacar? R$ '))

while True:

    if valor_a_sacar >= 50:
        notas_cinquenta = valor_a_sacar // 50
        print(f'Total de {notas_cinquenta} cédulas de R$ 50,00')
        valor_a_sacar -= notas_cinquenta * 50

    if valor_a_sacar >= 20:
        notas_vinte = valor_a_sacar // 20
        print(f'Total de {notas_vinte} cédulas de R$ 20,00')
        valor_a_sacar -= notas_vinte * 20

    if valor_a_sacar >= 10:
        notas_dez = valor_a_sacar // 10
        print(f'Total de {notas_dez} cédulas de R$ 10,00')
        valor_a_sacar -= notas_dez * 10

    if valor_a_sacar >= 1:
        notas_um = valor_a_sacar // 1
        print(f'Total de {notas_um} cédulas de R$ 1,00')
        valor_a_sacar -= notas_um * 1

    print(34 * '=')
    break

print('Volte sempre ao banco CEV. Tenha um bom dia!')
