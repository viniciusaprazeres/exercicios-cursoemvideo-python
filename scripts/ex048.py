soma = quantiade = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        quantiade+= 1

print(f'A soma de todos os {quantiade} de valores solicitados é {soma}.')
