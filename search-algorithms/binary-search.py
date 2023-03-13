import sys

sys.path.append('/media/alvaro/Arquivos/Python Projects/algorithms')

from timer import timer, timeit
from sample import sample

@timeit
def binary_search(L, x, start, end):    

    middle = start + (end - start) // 2

    if start > end:
        return -1

    elif L[middle] == x:
        return middle

    elif L[middle] > x:
        return binary_search(L, x, start, middle-1)

    else:
        return binary_search(L, x, middle+1, end)


if __name__ == '__main__':

    print(binary_search(sorted(sample), 72, 0, len(sample)))    