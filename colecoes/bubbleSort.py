def bubbleSort(lista):
    for j in range(len(lista)):
        for i in range(len(lista)-1 -j):
                if lista[i] > lista[i+1]:
                   lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista


              


l = [2, 8, 5, 4, 10, 0]
bubbleSort(l)
print(l)

