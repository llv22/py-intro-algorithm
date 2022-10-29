from typing import List, Any
import numpy as np

def partition(A: List[Any], l: int, r: int):
    i = np.random.randint(l, r+1)
    

def quicksort(A: List[Any], l: int, r: int):
    if l < r:
        q = partition(A, l, r)
        quicksort(A, l, q-1)
        quicksort(A, q+1, r)

if __name__ == "__main__":
    A = np.random.rand(20)
    quicksort(A, 0, len(A))
