pesos = []

for i in range(0, 5):
    pesos.append(float(input(f"Peso da {i + 1} pessoa (kg): ")))

maior = max(pesos)
menor = min(pesos)

print(f'O maior peso é de {maior}.')
print(f'O menor peso é de {menor}.')
