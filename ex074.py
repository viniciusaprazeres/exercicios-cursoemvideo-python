from random import randint

valores = []

for i in range(0, 5):
    valores.append(randint(1, 100))

print(f'Os valores sorteados foram: {valores}')
print(f'O maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')
