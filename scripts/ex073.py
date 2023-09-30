times_brasileirao = ['Fluminense', 'Athletico-PR', 'Palmeiras', 'Bahia', 'São Paulo', 'América-MG', 'Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Corinthians', 'Atlético-MG', 'Vasco da Gama', 'Fortaleza ', 'Internacional', 'Botafogo', 'Bragantino', 'Santos', 'Goiás', 'Grêmio']
times_brasileirao_ordenados = sorted(times_brasileirao)

print(164 * '=')
print(f'Times do Brasileirão 2023: {times_brasileirao}')
print(164 * '=')
print(f'Os 5 primeiros times são: {times_brasileirao[:5]}')
print(164 * '=')
print(f'Os 5 últimos times são: {times_brasileirao[-5:]}')
print(164 * '=')
print(f'Times em ordem alfabética: {times_brasileirao_ordenados}')
print(164 * '=')
print(f'O Vasco está na posição {times_brasileirao.index("Vasco da Gama")}.')