#Faça um programa que leia o nome e média de um aluno
#guardando também a situação em um dicionário
#no final, mostre o conteúdo na tela

aluno = []

nome = str(input("Nome: "))
media = float(input("media: "))

aluno["Nome"] = nome
aluno["Media"] = media



if aluno["Media"] < 7:
    print("Situação é igual a Reprovado")
else :
    print("Situação é igual a Aprovado")