numero = contador = soma = maior = menor = 0
resposta = 's'

while resposta != 'n' and resposta != 'N' and resposta == 's' or resposta == 'S':
    numero = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N] '))
    soma += numero
    contador += 1

    if numero > maior and contador != 1:
        maior = numero
    elif numero < menor and contador != 1:
        menor = numero
    elif contador == 1:
        maior = menor = numero

print(f'Você digitou {contador} números e a média entre eles foi {(soma/contador):.2f}.')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')
