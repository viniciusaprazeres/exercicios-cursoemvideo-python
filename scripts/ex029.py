velocidade = float(input('Qual a velocidade atual do carro (km/h)?: '))

if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança.')
elif velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Multado! Você excedeu o limite de velocidade de 80 km/h.')
    print(f'Você deve pagar uma multa de R$ {multa}.')
else:
    print('Erro! Digite um número válido.')
