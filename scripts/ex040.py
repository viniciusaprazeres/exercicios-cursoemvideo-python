primeira_nota = float(input('Primeira nota: '))
segunda_nota = float(input('Segunda nota: '))
media = (primeira_nota + segunda_nota) / 2

print(f'Tirando {primeira_nota:.1f} e {segunda_nota:.1f} a média do aluno será {media:.1f}')

if media < 5:
    print('O aluno está REPROVADO!')
elif 5 <= media < 7:
    print('O aluno está em RECUPERAÇÂO!')
else:
    print('O aluno está APROVADO')
