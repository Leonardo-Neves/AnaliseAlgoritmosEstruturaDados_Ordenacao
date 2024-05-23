import random
import sys
from numba import njit

sys.setrecursionlimit(100001)
class QuickSort:

    def __init__(self, array):
        self.array = array

    def sort(self):
        n = len(self.array)
        self.quicksort_ordena(0, n - 1)
        return self.array
    
    # def quicksort_ordena(self, p, r):
    #     if p < r:
    #         q = self.particiona(p, r)
            
    #         if p < (q-1):
    #             self.quicksort_ordena(p, q-1)
            
    #         if (q+1) < r:
    #             self.quicksort_ordena(q+1, r)
    
    def quicksort_ordena(self, p, r):
        while p < r:
            q, t = self.quicksort_particao_ternaria(p, r)
            if (q - p < r - t):
                self.quicksort_ordena(p, q - 1)
                p = t + 1 
            else:
                self.quicksort_ordena(t + 1, r)
                r = q - 1
                
    def particiona(self, p, r):
        pivot = self.array[r]
        i = p - 1
        
        for j in range(p, r):
            if (self.array[j] <= pivot):
                i += 1
                aux = self.array[j]
                self.array[j] = self.array[i]
                self.array[i] = aux
        aux = self.array[r]
        self.array[r] = self.array[i+1]
        self.array[i+1] = aux
    
        return i+1
    
    def quicksort_particao_ternaria(self, p, r):
        x = self.array[r]
        i = p - 1
        k = r
        j = p
        
        while(j <= k - 1):
            if self.array[j] < x:
                i += 1
                aux = self.array[i]
                self.array[i] = self.array[j]
                self.array[j] = aux
            elif self.array[j] == x:
                k -= 1
                aux = self.array[k]
                self.array[k] = self.array[j]
                self.array[j] = aux
                j -= 1
            j += 1
        q = i + 1
        for j in range(k, r + 1):
            i += 1
            aux = self.array[i]
            self.array[i] = self.array[j]
            self.array[j] = aux
        t = i
        
        return q, t
            
@njit(parallel=True)
def quickSort(array):
    n = len(array)
    quicksort_ordena(array, 0, n - 1)
    return array

@njit(parallel=True)
def quicksort_ordena(array, p, r):
    while p < r:
        array, q, t = quicksort_particao_ternaria(array, p, r)
        if (q - p < r - t):
            quicksort_ordena(array, p, q - 1)
            p = t + 1 
        else:
            quicksort_ordena(array, t + 1, r)
            r = q - 1
            
@njit(parallel=True)
def quicksort_particao_ternaria(array, p, r):
    x = array[r]
    i = p - 1
    k = r
    j = p
    
    while(j <= k - 1):
        if array[j] < x:
            i += 1
            aux = array[i]
            array[i] = array[j]
            array[j] = aux
        elif array[j] == x:
            k -= 1
            aux = array[k]
            array[k] = array[j]
            array[j] = aux
            j -= 1
        j += 1
    q = i + 1
    for j in range(k, r + 1):
        i += 1
        aux = array[i]
        array[i] = array[j]
        array[j] = aux
    t = i
    
    return array, q, t