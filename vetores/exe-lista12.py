matriz = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        matriz[i][j] = int(input("Digite um numero: ")) 

soma = 0
contador = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        soma += matriz[linha][coluna]
        contador += 1

media = soma / contador
print("Média:", media)