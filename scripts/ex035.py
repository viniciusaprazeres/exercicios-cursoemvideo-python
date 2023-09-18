print(10 * '=' + ' Analisador de Triângulos ' + 10 * '=')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('Os segmentos digitados PODEM FORMAR UM TRIÂNGULO.')
else:
    print('Os segmentos digitados NÃO PODEM FORMAR UM TRIÂNGULO.')
