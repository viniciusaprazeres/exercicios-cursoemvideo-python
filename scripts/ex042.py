a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    if a == b == c:
        print('Os segmentos digitados PODEM FORMAR UM TRIÂNGULO EQUILÁTERO.')
    elif a == b or a == c or b == c:
        print('Os segmentos digitados PODEM FORMAR UM TRIÂNGULO ISÓSCELES.')
    else:
        print('Os segmentos digitados PODEM FORMAR UM TRIÂNGULO ESCALENO.')
else:
    print('Os segmentos digitados NÃO PODEM FORMAR UM TRIÂNGULO.')
