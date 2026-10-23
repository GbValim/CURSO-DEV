# Desenvolva um script que abra o arquivo alunos.txt gerado no exercício
# anterior. O programa deve exibir na tela os nomes dos alunos formatados em
# ordem numérica (ex: 1 - Aluno) e, ao final, imprimir o total de registros lidos.

with open("alunos.txt",'r', encoding='utf-8') as f:
    for linha in f :
         conteudo = linha.strip()
         print(conteudo)

