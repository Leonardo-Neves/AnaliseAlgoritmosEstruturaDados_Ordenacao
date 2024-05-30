import random
from numba import njit

@njit(parallel=True)
def bubbleSort(array):

    counter_comparisons, counter_moviments = 0, 0

    n = len(array)
    n_trocas = 0
    counter_moviments += 2
    
    for i in range(0, n-1):
        for j in range(1, n-i):
            if array[j] < array[j-1]:
                counter_comparisons += 1

                aux = array[j]
                array[j] = array[j-1]
                array[j-1] = aux
                n_trocas += 1
                counter_moviments += 4
        
        if n_trocas == 0:
            counter_comparisons += 1
            break
    
    return array, counter_comparisons, counter_moviments

class BubbleSort:

    def __init__(self, array):
        self.array = array
    
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
            
