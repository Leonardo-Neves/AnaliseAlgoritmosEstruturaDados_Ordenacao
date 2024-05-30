import random
from numba import njit

class SelectionSort:

    def __init__(self, array):
        self.array = array

    def sort(self):

        A = self.array

        i, aux, n = 0, 0, len(self.array)

        while i < (n - 1):

            j, min = i + 1, i

            while j < n:

                if A[j] < A[min]:
                    min = j

                j = j + 1
            
            if i != min:
                aux = A[min]
                A[min] = A[i]
                A[i] = aux

            i = i + 1
        return A

@njit(parallel=True)
def selectionSort(array):

    A = array
    
    aux, n = 0, len(array)

    for i in range(0, (n - 1)):

        min = i
        
        for j in range(i + 1, n):

            if A[j] < A[min]:
                min = j
        
        if i != min:
            aux = A[min]
            A[min] = A[i]
            A[i] = aux

    return A

