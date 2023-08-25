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

#Função para merge
def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0

    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right += 1
        
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left += 1

        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left += 1
        else:
            lista[k] = right[top_right]
            top_right += 1

def merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)

    if(fim - inicio > 1):
        meio = (inicio + fim)//2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    
    return lista

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

def quick_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quick_sort(lista, inicio, p-1)
        quick_sort(lista, p+1, fim)
    
    return lista