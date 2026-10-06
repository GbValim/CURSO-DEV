# Desenvolva um programa que solicite o preenchimento de uma matriz 3 × 3 com
# números inteiros e, em seguida, peça ao usuário um valor numérico constante
# (escalar). Utilizando laços de repetição aninhados, o programa deve multiplicar cada
# elemento da matriz original por esse valor escalar e exibir a matriz resultante
# formatada em linhas e colunas.
import copy
matriz = []
novaMatriz = []
# criando a matriz
for i in range (3):
    coluna = []
    for j in range (3):
        posicao = int(input(f"digite o{i}º numero"))
        coluna.append(posicao)
    matriz.append(coluna)

escalar = int(input(f"Escreva um valor numerico para calculo"))


novaMatriz = copy.deepcopy(matriz)
for k in range (3):
    for l in range (3):
        novaMatriz[k][l] = matriz[k][l] * escalar


for m in range (3):
    for n in range (3):
        print(f"{novaMatriz[m][n]}", end="\t")
    print()








