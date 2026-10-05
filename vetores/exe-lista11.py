#Construa uma página onde o usuário digitará o nome e a média de cinco
#alunos e o programa só aceitará a média do aluno caso ela esteja entre zero
#e dez.

lista = []

for i in range(5):
    nome = input("digite o nome: \n")
    media = input("digite a media: \n")
    while media < 0 or media > 10:
        print("numero fora da media")
print("media igual a: " + media)