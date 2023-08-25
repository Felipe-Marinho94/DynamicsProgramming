'''
Recursão em python
Autor:Felipe Pinto Marinho
Data:25/08/2023
'''

#Fatorial
def fatorial(n:int) -> int:
    
    #Caso base
    if n == 1:
        return 1
    
    #Caso recursivo
    return n * fatorial(n - 1)

if __name__ == "__main__":
    fat5 = fatorial(800)
    print(fat5)