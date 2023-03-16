soma_pares = quantidade_pares = 0

for i in range(1, 7):
    numero = int(input(f'Digite um {i}° valor: '))

    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1
print(f'Você informou {quantidade_pares} valores pares e a soma é {soma_pares}.')
