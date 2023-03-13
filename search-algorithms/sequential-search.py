import sys

sys.path.append('/media/alvaro/Arquivos/Python Projects/algorithms')

from timer import timer
from sample import sample

@timer
def senquential_search(L, x):
    control = False
    i = 0
    while i < len(L) and not control:
        if (L[i] == x):
            control = True
            pos = i
        else:
            i += 1
    
    if control:
        return pos
    else:
        return control

if __name__ == '__main__':

    senquential_search(sample, sample[-1])