'''
Algoritmo de ordenação - SELECTION SORT
Autor:Felipe Pinto Marinho
Data:24/08/2023
'''
def selection_sort(lista):

    for j in range(len(lista)-1):
        min_index = j

        #Determinação do índice do mínimo
        for i in range(j, len(lista)):
            if lista[i] < lista[min_index]:
                min_index = i
    
        #Permutação das posições
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
    
    return lista

def bubble_sort(lista):
    for j in range(len(lista) - 1):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    
    return lista

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    
    return lista

