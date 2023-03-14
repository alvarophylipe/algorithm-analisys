import sys

sys.path.append('/media/alvaro/Arquivos/Python Projects/algorithms')

from timer import timer, timeit
from sample import sample

@timeit
def selection_sort(L):

    for i in range(len(L)):
        low = i
        for j in range(i+1, len(L)):
            if L[j] < L[low]:
                low = j
        
        L[low], L[i] = L[i], L[low]

if __name__ == '__main__':
    selection_sort(sample)