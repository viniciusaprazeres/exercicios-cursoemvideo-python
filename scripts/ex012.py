preco_inicial = float(input('Qual é o preço do produto? R$ '))
desconto = (5/100) * preco_inicial
preco_final = preco_inicial - desconto

print(f'O produto custava R$ {preco_inicial:.2f}, na promoção com desconto de 5% vai custar R$ {preco_final:.2f}.')