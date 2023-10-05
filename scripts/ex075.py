numeros = []
pares = []

numeros.append(int(input('Digite um número: ')))
numeros.append(int(input('Digite outro número: ')))
numeros.append(int(input('Digite mais um número: ')))
numeros.append(int(input('Digite o último número: ')))

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.' if 9 in numeros else 'O valor 9 não foi digitado.')
print(f'O primeiro ou único valor 3 apareceu na posição {numeros.index(3) + 1}' if 3 in numeros else "O valor 3 não foi digitado.")
print(f'Os valores pares digitados foram: {pares}.')
