# Desenvolva um programa em Python que leia 10 números inteiros e os armazene em um vetor
# original. A partir dessa estrutura, crie duas novas listas independentes: uma lista denominada pares,
# contendo cada número par do vetor original multiplicado por 3, e uma lista denominada ímpares,
# contendo os números ímpares mantidos com seus valores inalterados. Ao final, o programa deve
# exibir o vetor original, os dois novos vetores resultantes e a contagem exata de elementos alocados
# em cada um deles.

lista = []
listaPares = []
listaImpares = []

# fazendo a lista original
for i in range (10):
    numero = int(input("Digite um numero"))
    lista.append(numero)
# lista dos pares
for numero in lista:
    if numero % 2 == 0:
        listaPares.append(numero * 3)

#lista dos impares
for numero in lista:
    if numero % 2 == 1:
        listaImpares.append(numero)

listaComp = len(lista)
listaImpComp = len(listaImpares)
listaParComp = len(listaPares)


print(f"{lista}\n")
print(f"{listaPares}\n")
print(f"{listaImpares}\n")


