numeros_por_extenso = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 
                       'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 
                       'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
                        'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte']

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número: {numeros_por_extenso[numero]}.')
        break
    else:
        print(f'Erro. Digite novamente!')