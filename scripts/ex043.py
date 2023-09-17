peso = float(input('Qual é o seu peso (kg)? '))
altura = float(input('Qual a sua altura (m)? '))
imc = peso / (altura**2)

print(f'O IMC dessa pessoa é {imc:.1f}')

if imc < 18.5:
    print('ATENÇÃO. Você está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('PARABÉNS! Você está na faixa de peso IDEAL.')
elif 25 <= imc < 30:
    print('ATENÇÃO! Você está na faixa de SOBREPESO.')
elif 30 <= imc < 40:
    print('ATENÇÃO! Você está na faixa de OBESIDADE.')
elif 40 <= imc:
    print('CUIDADO! Você está na faixa de OBESIDADE MÓRBIDA.')
else:
    print('Digite peso e altura válidos!')
