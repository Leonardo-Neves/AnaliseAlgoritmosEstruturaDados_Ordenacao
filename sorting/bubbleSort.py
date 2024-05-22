from numba import jit
import random

class BubbleSort:

    def __init__(self, array):
        self.array = array
    
    @jit(nopython=True, parallel=True)
    def sort(self):
        n = len(self.array)
        n_trocas = 0
        
        for i in range(0, n-1):
            j = 1
            while(j < n - i):
                if (self.array[j] < self.array[j-1]):
                    aux = self.array[j]
                    self.array[j] = self.array[j-1]
                    self.array[j-1] = aux
                    n_trocas += 1
                j += 1 
            
            if n_trocas == 0:
                break
        
        return self.array
            
if __name__ == "__main__":
    n = 20
    itens = [random.randint(1, 100) for i in range(0, n)]

    print('itens', itens)

    sort_algorithm = BubbleSort(itens)
    itens_sorted = sort_algorithm.sort()

    print('itens_sorted', itens_sorted)