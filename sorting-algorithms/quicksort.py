import sys

sys.path.append('/media/alvaro/Arquivos/Python Projects/algorithms')

from timer import timer, timeit
from sample import sample

@timeit
def quick_sort(L):
    if len(L) <= 1:
        return L
    
    m = L[0]
    return quick_sort([x for x in L if x < m]) + \
                        [x for x in L if x == m] + \
            quick_sort([x for x in L if x > m])





if __name__ == '__main__':
    quick_sort(sample)