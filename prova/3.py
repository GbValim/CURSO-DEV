# Construa um programa em Python que receba os dados para preencher uma matriz 3x3 com
# números inteiros informados pelo usuário. Após o preenchimento, o sistema deve solicitar um valor
# numérico de corte (limiar). O programa deve varrer a matriz, contabilizar quantos elementos são
# estritamente maiores que esse limiar e gerar uma segunda matriz 3x3 onde todos os valores
# superiores ao limiar sejam substituídos por 0, mantendo os demais inalterados. Ao final, exiba a
# contador de elementos acima do limiar e a matriz resultante formatada em linhas e colunas.
matriz = []
novaMatriz = []

# criando a matriz
for i in range (3):
    coluna = []
    for j in range (3):
        posicao = int(input(f"digite o {i+1}º numero"))
        coluna.append(posicao)
    matriz.append(coluna)

#Fazendo a matriz nova
limiar = int(input(f"Escreva um valor numerico para calculo"))
print("Matriz original:")
for m in range (3): 
    for n in range (3):
        print(f"{matriz[m][n]}", )
     

print(f"Limiar: {limiar}")
contador = 0

#verificação se numero é maior que zero
for m in range (3):
    coluna = []
    for n in range (3):
        if matriz[m][n] > limiar:
            coluna.append(0)
            contador += 1
        else:
            coluna.append(matriz[m][n])
    novaMatriz.append(coluna)

#escrevendo a nova matriz atualizada
for m in range (3):
    for n in range (3):
        print(f"{novaMatriz[m][n]}", )
    
