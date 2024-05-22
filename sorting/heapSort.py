import random
import sys
from numba import jit

sys.setrecursionlimit(100001)

class HeapSort:
    def __init__(self, array, minimum=False):
        self.A = array
        self.minimum = minimum

    @jit(parallel=True)
    def reDoMinimum(self, A, n, i):
        smallest = int(i)
        l = int(2 * i + 1)
        r = int(2 * i + 2)
    
        if l < n and A[l] < A[smallest]:
            smallest = l
        
        if r < n and A[r] < A[smallest]:
            smallest = r
        
        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            A = self.reDoMinimum(A, n, smallest)

        return A

    @jit(parallel=True)
    def buildMinimum(self, A, n):

        i = n / 2 - 1
        while i >= 0:
            A = self.reDoMinimum(A, int(n), int(i))
            i = i - 1

        return A

    @jit(parallel=True)
    def reDoMaximum(self, A, esq, dir):
        i = esq
        j = i * 2 + 1

        aux = A[i]
        while (j <= dir):
            if ((j < dir) and (A[j] < A[j + 1])):
                j = j + 1
            if (aux >= A[j]):
                break
            A[i] = A[j]
            i = j
            j = i * 2 + 1
        
        A[i] = aux

        return A

    @jit(parallel=True)
    def buildMaximum(self, A, n):
        esq = int((n / 2) - 1)
        
        while (esq >= 0):
            A = self.reDoMaximum(A, esq, n-1)
            esq = esq - 1

        return A

    @jit(parallel=True)
    def sort(self):

        if self.minimum:
            A = self.buildMinimum(self.A, len(self.A))
            
            i = len(self.A) - 1
            while i >= 0:
                A[0], A[i] = A[i], A[0]
                self.reDoMinimum(A, int(i), 0)
                i = i - 1

            return A

        elif not self.minimum:

            A = self.buildMaximum(self.A, len(self.A))

            m = len(A) - 1

            while (m > 0):
                aux = A[m]
                A[m] = A[0]
                A[0] = aux
                m = m - 1
                A = self.reDoMaximum(A, 0, m)

            return A

# n = 10
# itens = [random.randint(1, n) for i in range(0, n)]

# print('itens', itens)

# heap_short = HeapSort(itens, minimum=False)
# itens_sorted = heap_short.sort()

# print('itens_sorted', itens_sorted)