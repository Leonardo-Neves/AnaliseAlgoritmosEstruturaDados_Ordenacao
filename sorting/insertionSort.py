from numba import jit
import random

class InsertionSort:

    def __init__(self, array):
        self.array = array

    @jit(nopython=True, parallel=True)
    def sort(self):
        for i in range(1, len(self.array)):
            aux = self.array[i]
            j = i - 1
            
            while((j >= 0) and (aux < self.array[j])):
                self.array[j+1] = self.array[j]
                j -= 1
            self.array[j+1] = aux
        
        return self.array
            
if __name__ == "__main__":
    n = 20
    itens = [random.randint(1, 100) for i in range(0, n)]

    print('itens', itens)

    sort_algorithm = InsertionSort(itens)
    itens_sorted = sort_algorithm.sort()

    print('itens_sorted', itens_sorted)