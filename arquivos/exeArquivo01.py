alunos = []

for numero in range(1, 4):
    nome = input(f'Informe o nome do aluno {numero}: ')
    alunos.append(nome)


with open('alunos.txt', 'w', encoding='utf-8') as arquivo:
    for nome in alunos:
        arquivo.write(f'{nome}\n')
