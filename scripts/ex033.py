primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))

if primeiro > segundo:
    auxiliar = segundo
    segundo = primeiro
    primeiro = auxiliar

if segundo > terceiro:
    auxiliar = terceiro
    terceiro = segundo
    segundo = auxiliar

if primeiro > segundo:
    auxiliar = segundo
    segundo = primeiro
    primeiro = auxiliar

print(f'O menor valor digitado foi {primeiro}')
print(f'O maior valor digitado foi {terceiro}')
