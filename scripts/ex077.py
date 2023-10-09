palavras = ['APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',  
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 
            'MERCADO', 'PROGRAMADOR', 'FUTURO']

vogais = []

for palavra in palavras:
    for letra in palavra:
        if 'A' == letra:
            vogais.append('A')
        if 'E' == letra:
          vogais.append('E')
        if 'I' == letra:
           vogais.append('I')
        if 'O' == letra:
            vogais.append('O')
        if 'U' == letra:
            vogais.append('U')

    print(f'Na palavra {palavra} temos as vogais: {vogais}')
    vogais.clear()

        