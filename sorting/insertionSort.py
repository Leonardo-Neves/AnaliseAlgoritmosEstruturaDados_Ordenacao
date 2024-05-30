import random
from numba import njit

class InsertionSort:

    def __init__(self, array):
        self.array = array

    def sort(self):
        for i in range(1, len(self.array)):
            aux = self.array[i]
            j = i - 1
            
            while((j >= 0) and (aux < self.array[j])):
                self.array[j+1] = self.array[j]
                j -= 1
            self.array[j+1] = aux
        
        return self.array
            

@njit(parallel=True)
def insertionSort(array):

    counter_comparisons, counter_moviments = 0, 0

    for i in range(1, len(array)):
        aux = array[i]
        j = i - 1
        counter_moviments += 2
        
        for k in range(j, -1, -1):
            if aux < array[k]:
                counter_comparisons += 1

                array[k+1] = array[k]
                counter_moviments += 1
            else:
                counter_comparisons += 1

                k += 1
                counter_moviments += 1
                break
        else:
            k = 0
            counter_moviments += 1
        
        array[k] = aux
        counter_moviments += 1
    
    return array, counter_comparisons, counter_moviments