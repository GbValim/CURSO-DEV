# Imagine que você foi contratado para criar um pequeno sistema de controle acadêmico para uma escola.
# O seu programa deve armazenar e processar informações de alunos e suas respectivas notas utilizando dicionários.

# Escreva um script em Python que realize as seguintes
# operações utilizando um dicionário principal chamado escola
# (ou a estrutura que preferir):

# Exemplo: {"Alice": [8.5, 9.0, 7.5], "Bruno": [6.0, 5.5, 7.0], "Carla": [9.5, 10.0, 9.0]}



aluno = {}
contador = 0

while contador < 3:
    nomeAluno = str(input("Digite o nome do primeiro aluno: "))
    aluno["nome"] = nomeAluno

    nota01 = (input("Digite a primeira nota do aluno: "))
    aluno["nota01"] = nota01

    nota02 = (input("Digite a primeira nota do aluno: "))
    aluno["nota02"] = nota02

    nota03 = (input("Digite a primeira nota do aluno: "))
    aluno["nota03"] = nota03
    contador += 1




# Função de Cálculo de Média: Crie uma função que receba o dicionário e calcule a média aritmética de cada aluno,
# retornando um novo dicionário onde a chave é o nome do aluno e o valor é a sua média final.

def calculaMedia():
    soma = (nota01 + nota02 + nota03) / 3
    return soma 

