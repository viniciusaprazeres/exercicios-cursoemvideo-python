numero = 0
contador = 0
soma = 0

while numero != 999:
    numero = int(input('Digite um número [999 para parar o programa]: '))
    if numero == 999:
        break
    else:
        contador += 1
        soma += numero

print(f'A soma dos {contador} valores foi {soma}.')
