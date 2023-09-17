valor_casa = float(input('Valor da casa R$: '))
salario_comprador = float(input('Salário do comprador R$: '))
anos_financiamento = int(input('Anos de financiamento:  '))
prestacao = valor_casa / (anos_financiamento * 12)

if prestacao <= 0.3 * salario_comprador:
    print(f'Para pagar uma casa de R$ {valor_casa:.2f} em {anos_financiamento} anos, a parcela será de R$ {prestacao:.2f} por mês. Empréstimo APROVADO!')
else:
    print(f'Para pagar uma casa de R$ {valor_casa:.2f} em {anos_financiamento} anos, a parcela será de R$ {prestacao:.2f} por mês. Empréstimo NEGADO!')