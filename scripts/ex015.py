dias = float(input(f'Quantos dias o carro foi alugado? '))
quilometros = float(input(f'Quantos quilômetros foram rodados? '))
total = 60 * dias + 0.15 * quilometros

print(f'O total a pagar é de R$ {total:.2f}.')
