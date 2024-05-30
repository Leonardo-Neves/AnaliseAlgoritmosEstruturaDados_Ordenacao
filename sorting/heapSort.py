import random
import sys
from numba import njit

sys.setrecursionlimit(100001)

class HeapSort:
    def __init__(self, array, minimum=False):
        self.A = array
        self.minimum = minimum

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

    def buildMinimum(self, A, n):

        i = n / 2 - 1
        while i >= 0:
            A = self.reDoMinimum(A, int(n), int(i))
            i = i - 1

        return A

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

    def buildMaximum(self, A, n):
        esq = int((n / 2) - 1)
        
        while (esq >= 0):
            A = self.reDoMaximum(A, esq, n-1)
            esq = esq - 1

        return A
    
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

@njit(parallel=True)
def reDoMinimum(A, n, i, counter_comparisons, counter_moviments):
    smallest = int(i)
    l = int(2 * i + 1)
    r = int(2 * i + 2)
    counter_moviments += 3

    counter_comparisons += 1
    if l < n and A[l] < A[smallest]:
        smallest = l
        counter_moviments += 1
    
    counter_comparisons += 1
    if r < n and A[r] < A[smallest]:
        smallest = r
        counter_moviments += 1
    
    counter_comparisons += 1
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        A, counter_comparisons, counter_moviments = reDoMinimum(A, n, smallest, counter_comparisons, counter_moviments)
        counter_moviments += 3

    return A, counter_comparisons, counter_moviments

@njit(parallel=True)
def buildMinimum(A, n, counter_comparisons, counter_moviments):
    for i in range(int(n // 2) - 1, -1, -1):
        A, counter_comparisons, counter_moviments = reDoMinimum(A, int(n), int(i), counter_comparisons, counter_moviments)
        counter_moviments += 1
    return A, counter_comparisons, counter_moviments

@njit(parallel=True)
def reDoMaximum(A, esq, dir, counter_comparisons, counter_moviments):
    i = esq
    j = i * 2 + 1

    aux = A[i]
    counter_moviments += 3

    while (j <= dir):
        counter_comparisons += 1

        if ((j < dir) and (A[j] < A[j + 1])):
            counter_comparisons += 1
            j = j + 1
            counter_moviments += 1

        if (aux >= A[j]):
            counter_comparisons += 1
            break

        A[i] = A[j]
        i = j
        j = i * 2 + 1
        counter_moviments += 3
    
    A[i] = aux
    counter_moviments += 1

    return A, counter_comparisons, counter_moviments

@njit(parallel=True)
def buildMaximum(A, n, counter_comparisons, counter_moviments):
    for esq in range(int((n // 2) - 1), -1, -1):
        A, counter_comparisons, counter_moviments = reDoMaximum(A, esq, n-1, counter_comparisons, counter_moviments)
        counter_moviments += 1

    return A, counter_comparisons, counter_moviments

@njit(parallel=True)
def heapSort(A, minimum=False):

    counter_comparisons, counter_moviments = 0, 0

    if minimum:
        A, counter_comparisons, counter_moviments = buildMinimum(A, len(A), counter_comparisons, counter_moviments)
        for i in range(len(A) - 1, -1, -1):
            A[0], A[i] = A[i], A[0]
            counter_moviments += 2

            A, counter_comparisons, counter_moviments = reDoMinimum(A, int(i), 0, counter_comparisons, counter_moviments)
            
        return A, counter_comparisons, counter_moviments
    else:
        A, counter_comparisons, counter_moviments = buildMaximum(A, len(A), counter_comparisons, counter_moviments)
        for m in range(len(A) - 1, 0, -1):
            A[m], A[0] = A[0], A[m]
            counter_moviments += 2

            A, counter_comparisons, counter_moviments = reDoMaximum(A, 0, m - 1, counter_comparisons, counter_moviments)

        return A, counter_comparisons, counter_moviments