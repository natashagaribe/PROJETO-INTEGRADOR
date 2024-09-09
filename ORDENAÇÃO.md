ORDENAÇÃO
Aqui está um código Python que implementa o algoritmo de ordenação Bubble Sort:

def bubble_sort(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista

sequencia = [64, 34, 25, 12, 22, 11, 90]
print("Sequência original:", sequencia)
ordenada = bubble_sort(sequencia)
print("Sequência ordenada:", ordenada)

![image](https://github.com/user-attachments/assets/19c75ad5-91d5-49e1-9dd4-358b16474605)
