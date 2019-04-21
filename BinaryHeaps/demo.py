from BinaryHeaps.MaxHeap import Heap


heap=Heap()
heap.insert(10)
heap.insert(40)
heap.insert(23)
heap.insert(43)
heap.insert(65)
heap.insert(64)
heap.insert(232)
heap.insert(98)
heap.insert(99)
heap.insert(78)
heap.insert(61)
heap.insert(22)
for i in range(0,heap.current_position+1):
    print(heap.heap[i]," ", i)