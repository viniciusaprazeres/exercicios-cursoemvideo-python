from math import factorial

numero = int(input('Digite um número para calcular seu fatorial: '))
etapas = numero
resultado = factorial(numero)

print(f'Calculando {numero}! = ', end='')

while etapas > 0:
    print(f'{etapas}', end='')
    print(' x ' if etapas > 1 else ' = ', end='')
    etapas -= 1

print(f'{resultado}')
