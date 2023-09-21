numero_inteiro = int(input('Digite um número inteiro: '))
print('Digite uma base para conversão:')
print('[ 1 ] Converter para BINÁRIO.')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL.')
opcao = int(input('Qual a sua opção?: '))

if opcao == 1:
    print(f'{numero_inteiro} convertido para BINÁRIO: {bin(numero_inteiro)[2:]}')
elif opcao == 2:
    print(F'{numero_inteiro} convertido para OCTAL: {oct(numero_inteiro)[2:]}')
elif opcao == 3:
    print(F'{numero_inteiro} convertido para HEXADECIMAL: {hex(numero_inteiro)[2:]}')
else:
    print('Erro! Digite uma opção válida.')
