import sys

sys.path.append('/media/alvaro/Arquivos/Python Projects/algorithms')

from timer import timer, timeit
from sample import sample

@timeit
def bubble_sort(L):

    for i in range(len(L)-1, 0, -1):
        for j in range(i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

if __name__ == '__main__':
    bubble_sort(sample)