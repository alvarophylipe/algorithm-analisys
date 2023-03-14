import sys

sys.path.append('/media/alvaro/Arquivos/Python Projects/algorithms')

from timer import timer, timeit
from sample import sample

@timeit
def insertion_sort(L):
    
    for i in range(len(L)):
        k = i
        while k > 0 and L[k] < L[k-1]:
            L[k], L[k-1] = L[k-1], L[k]
            k -= 1

if __name__ == '__main__':
    insertion_sort(sample)