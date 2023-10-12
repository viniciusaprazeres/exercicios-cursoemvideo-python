numeros = []
indices_maior = []
indices_menor = []

for i in range(0, 5):
    numeros.append(input(f'Digite um número para a posição {i}: '))

maior = max(numeros)
menor = min(numeros)

for indice, numero in enumerate(numeros):
    if numero == maior:
        indices_maior.append(indice)
    if numero == menor:
        indices_menor.append(indice)

print(30 * '-=')

print(f'Você digitou os valores: {numeros}')

print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for posicao in indices_maior:
    print(f'{posicao}... ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições: ', end='')
for posicao in indices_menor:
    print(f'{posicao}... ', end='')
