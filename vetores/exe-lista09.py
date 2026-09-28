#Construa um programa que o usuário digitará o nome e a idade de dez
#pessoas e o programa escreverá o nome do usuário mais novo.

lista = []

for i in range  (0,4):
    nome = str(input("Digite o nome  "))
    idade = int(input("Digite a idade "))

    lista.append([nome,idade])

menorNumero = 0

for i in range (1, len(lista), 1):

    if lista[i][1] < lista[menorNumero][1]:
            menorNumero = i

print (f'o mais novo é: {lista[menorNumero][0]}')

    

