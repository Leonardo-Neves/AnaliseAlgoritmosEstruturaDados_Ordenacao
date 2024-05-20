
import random

class QuickSort:

    def __init__(self, array):
        self.array = array

    def sort(self):
        n = len(self.array)
        self.quicksort_ordena(0, n - 1)
        return self.array
    
    def quicksort_ordena(self, p, r):
        if p < r:
            q = self.particiona(p, r)
            self.quicksort_ordena(p, q-1)
            self.quicksort_ordena(q+1, r)
    
    def particiona(self, p, r):
        
        pivot = self.array[r]
        i = p - 1
        
        for j in range(p, r):
            if (self.array[j] <= pivot):
                i += 1
                aux = self.array[j]
                self.array[j] = self.array[i]
                self.array[i] = aux
        aux = self.array[r]
        self.array[r] = self.array[i+1]
        self.array[i+1] = aux
    
        return i+1
            
if __name__ == "__main__":
    n = 20
    itens = [random.randint(1, 100) for i in range(0, n)]

    print('itens', itens)

    sort_algorithm = QuickSort(itens)
    itens_sorted = sort_algorithm.sort()

    print('itens_sorted', itens_sorted)