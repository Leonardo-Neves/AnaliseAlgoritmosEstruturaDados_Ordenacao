import random
from numba import jit

class SelectionSort:

    def __init__(self, array):
        self.array = array

    @jit(nopython=True, parallel=True)
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

# n = 20
# itens = [random.randint(1, 100) for i in range(0, n)]

# print('itens', itens)

# selection_sort = SelectionSort(itens)
# itens_sorted = selection_sort.sort()

# print('itens_sorted', itens_sorted)
