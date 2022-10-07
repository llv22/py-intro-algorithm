import numpy as np
from typing import List, Any

def insertion_sort(A: List[Any]) -> List[Any]:
    """Insertion sorting for array with any type, which can be compared for each element.
    """
    for j in range(1, len(A)):
        key = A[j]
        # insert A[j] into the sorted sequence A[0,...,j-1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A

if __name__ == '__main__':
    sample_before_sort = np.random.uniform(low=0, high=10, size=(10,))
    print(f"Array before sorting is {sample_before_sort}")
    sample_after_sort = insertion_sort(sample_before_sort)
    print(f"Array after sorting is {sample_after_sort}")
