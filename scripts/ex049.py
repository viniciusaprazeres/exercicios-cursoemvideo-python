numero = int(input('Digite um número para ver sua tabuada: '))
print(' ')

for i in range(1, 11):
    print(f'{numero} x {i:2} = {numero * i}')
