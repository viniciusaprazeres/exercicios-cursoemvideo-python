distancia = float(input('Qual a distância (km) da sua viagem? '))


if distancia <= 200:
    passagem =  distancia * 0.5
else:
    passagem =  distancia * 0.45

print(f'Você está prestes a começar uma viagem de {distancia:.2f} km.')
print(f'E o preço da sua passagem será de R$ {passagem:.2f}')
