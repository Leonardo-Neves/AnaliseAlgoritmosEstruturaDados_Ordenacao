import random
import numpy as np

class MergeSort:

    def __init__(self, array, recursive):
        self.array = array
        self.recursive = recursive

    def interleave(self, A, initial_index, middle_index, end_index):

        B = [0 for i in range(0, (end_index - initial_index) + 1)]

        i = initial_index
        while i <= middle_index:
            B[i - initial_index] = A[i]
            i = i + 1

        j = middle_index + 1
        while j <= end_index:
            B[end_index + middle_index + 1 - j - initial_index] = A[j]
            j = j + 1

        i = initial_index
        j = end_index
        k = initial_index
        while k <= end_index:
            if B[i - initial_index] <= B[j - initial_index]:
                A[k] = B[i - initial_index]
                i = i + 1
            else:
                A[k] = B[j - initial_index]
                j = j - 1
            
            k = k + 1

        return A
    
    def sort(self):

        if self.recursive:
            
            i, aux, n = 0, 0, len(self.array)

            A = self.array

            while i < n:

                min = i
                j = i + 1 
                while j < n:    
                    if A[j] < A[min]:
                        min = j

                    j = j + 1   

                aux = A[min]
                A[min] = A[i]
                A[i] = aux

                i = i + 1

            return A

        elif not self.recursive:

            A = self.array

            initial_index, middle_index, end_index = 0, 0, 0

            n = len(self.array)

            i = 1
            while i < n:
                initial_index = 0
                while (initial_index + i) < n:
                    end_index = initial_index + (2 * i) - 1
                    if end_index >= n:
                        end_index = n - 1
                    middle_index = initial_index + i - 1
                    A = self.interleave(A, initial_index, middle_index, end_index)
                    initial_index = initial_index + (2 * i)
                i = 2 * i

            return A
        
# n = 20
# itens = [random.randint(1, 100) for i in range(0, n)]

# print('itens', itens)

# merge_sort = MergeSort(itens, recursive=True)
# itens_sorted = merge_sort.sort()

# print('itens_sorted', itens_sorted)
