A = [-4,3,1,0,2,5,10,8,12,9]
import heapq

heapq.heapify(A)
print(A)

#heap push
heapq.heappush(A,4)
print(A)

#heap pop
minn = heapq.heappop(A)
print(A)

#heap sort
def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n
    for i in range(n):
        minn = heapq.heappop(arr)
        print("minn", minn)
        new_list[i] = minn
    return new_list

print("res",heapsort([-4,3,1,0,2,5,10,8,12,9]))

#heap push pop
print(A)
heapq.heappushpop(A,99)

print(A)

#Max heap
B = [-4,3,1,0,2,5,10,8,12,9]
n = len(B)
for i in range(n):
    B[i] = -B[i]
heapq.heapify(B)
print("B",B)
heapq.heappush(B, -7) #Insert 7 into max heap

# Build heap from scratch

C= [-5,4,2,1,7,0,3]
heap = []
for x in C:
    heapq.heappush(heap,x)
    print(heap)

# Putting tuples of items on the heap
D = [5,4,3,5,4,3,5,5,4]
from collections import Counter

counter = Counter(D)

print(counter)

heap = []
for k,v in counter.items():
    heapq.heappush(heap,(v, k))
print(heap)