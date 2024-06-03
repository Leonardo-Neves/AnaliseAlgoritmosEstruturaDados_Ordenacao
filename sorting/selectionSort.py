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

    counter_comparisons = 0
    counter_moviments = 0

    for i in range(0, (n - 1)):

        min = i
        
        for j in range(i + 1, n):

            counter_comparisons += 1
            if A[j] < A[min]:
                min = j
                counter_moviments += 1
        
        counter_comparisons += 1
        if i != min:
            aux = A[min]
            A[min] = A[i]
            A[i] = aux
            counter_moviments += 3

    return A, counter_comparisons, counter_moviments