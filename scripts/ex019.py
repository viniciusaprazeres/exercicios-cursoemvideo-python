import random

primeiro_aluno = input("Primeiro aluno: ")
segundo_aluno = input("Segundo aluno: ")
terceiro_aluno = input("Terceiro aluno: ")
quarto_aluno = input("Quarto aluno: ")
nomes = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
random.shuffle(nomes)

print(f"O aluno escolhido foi {nomes}")
