numero = int(input('Digite um número [999 para parar]: '))
soma = 0
contador = 0

while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número [999 para parar]: '))

print(f'Você digitou {contador} números e a soma e a soma entre eles foi {soma}.')