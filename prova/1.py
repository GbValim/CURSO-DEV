# Em seguida, percorra a lista para calcular a média aritmética de todos os valores
# informados e determinar a quantidade de números pares presentes. Ao final da execução, o
# programa deve exibir a lista completa, o valor da média calculada e o total de elementos pares
# encontrados.


# solicita numeros
lista = []
total = 0
contador = 0
for i in range (6):
    numero = int(input("Digite um numero"))
    lista.append(numero)




#buscando pares
for numero in lista:
    total += numero
    if numero %2 == 0:
        contador += 1

# calculando média
media = total / len(lista)

#printando as respostas
print(f"Lista completa: {lista}")
print(f"A media média é: {media}")
print(f"A quantidade de numeros pares é: {contador}")
        

   

