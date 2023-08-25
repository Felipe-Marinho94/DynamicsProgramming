'''
Algoritmo de busca binária
Autor:Felipe Pinto Marinho
Data:25/08/2023
'''

#Busca binária
def binary_search(lista, item, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    
    if inicio <= fim:
        medio = (inicio + fim)//2
    
        if lista[medio] == item:
            return medio
    
        elif lista[medio] > item:
            return binary_search(lista, item, inicio, medio)
    
        else:
            return binary_search(lista, item, medio + 1, fim)
    
    return None
