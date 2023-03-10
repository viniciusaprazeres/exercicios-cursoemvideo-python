largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2

print(f'Sua parede tem dimensão de (2.5 x 1.75)m e sua área é de {area:.3f} metros quadrados.')
print(f'Para pintar essa parede, você precisará de {tinta:.4f}l de tinta.')