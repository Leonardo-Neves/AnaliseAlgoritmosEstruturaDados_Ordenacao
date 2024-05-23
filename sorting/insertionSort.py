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
    for i in range(1, len(array)):
        aux = array[i]
        j = i - 1
        
        while((j >= 0) and (aux < array[j])):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = aux
    
    return array