import math

angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo} tem SENO de {seno:.2f}')
print(f'O ângulo de {angulo} tem COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo} tem  TANGENTE de {tangente:.2f}')
