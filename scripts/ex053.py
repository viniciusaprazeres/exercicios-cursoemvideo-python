frase = input('Digite uma frase: ').lower()
palavra = frase.split()
juntas = ''.join(palavra)
palindromo = ''

for i in range(len(juntas) - 1, -1, -1):
    palindromo += juntas[i]

print(f'O inverso de {juntas} é {palindromo}.')
print('A palavra digitada É um PALÍNDROMO.' if juntas == palindromo else 'A palavra digitada NÃO É um PALÍNDROMO.')
