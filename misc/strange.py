from typing import List, Any
import numpy as np
import heapq
from heapq import heappush, heappop, heapify
from heapq_max import *

myMinHeap = []
myMaxHeap = []

def strange(A: List[Any], n: int) -> int:
    minSize = 0
    maxSize = 0
    
    for j in range(0, n):
        heappush(myMinHeap, A[j])
        minSize = len(myMinHeap)
        x = heappop(myMinHeap)
        minSize = len(myMinHeap)
        heappush_max(myMaxHeap, x)
        maxSize = len(myMaxHeap)
        if minSize < maxSize:
            y = heappop_max(myMaxHeap)
            maxSize = len(myMaxHeap)
            heappush(myMinHeap, y)
            minSize = len(myMinHeap)
    z = min(myMinHeap[0:minSize+1])
    return z

if __name__=="__main__":
    # A = np.random.rand(11)
    # for l in range(2, 20):
    l = 10
    A = list(range(l))
    print(f"A[0:{len(A)-1}]={A[0:len(A)]}, sorted A={sorted(A)} strange(A, {len(A)}) = {strange(A, len(A))}")