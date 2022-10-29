from typing import List, Any

def MaxHeapify(A: List[Any], heapSize: int, parent: int):
    # see: index should be adjusted due to the starting index with 1
    left = parent * 2 + 1
    right = parent * 2 + 2
    largest = parent
    if left < heapSize and largest < A[left]:
        largest = left
    if right < heapSize and largest < A[right]:
        largest = right
    if largest != parent:
        A[largest], A[parent] = A[parent], A[largest]
        MaxHeapify(A, heapSize, largest)   

def buildMaxHeap(A: List[Any], n: int):
    for i in range(n/2 + 1, 0, -1):
        MaxHeapify(A, len(A), i)

def heapSort(A: List[Any], l, r):
    pass

if __name__ == "__main__":
    A = np.random.rand(20)
    heapSort(A, 0, len(A))
