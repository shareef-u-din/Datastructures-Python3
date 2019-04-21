import math


class Heap:
    heap_size = 20

    def __init__(self):
        self.heap = [0] * Heap.heap_size
        self.current_position = -1

    @staticmethod
    def parent(index):
        return (index - 1) / 2

    @staticmethod
    def left(index):
        return (2 * index) + 1

    @staticmethod
    def right(index):
        return (2 * index) + 2

    def is_full(self):
        if self.current_position == Heap.heap_size:
            return False
        else:
            return True

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_leaf(self, index):
        n = self.current_position
        if n <= 0:
            return None
        leafs = math.floor(n / 2) + 1
        if index < leafs:
            return False
        else:
            return True

    def max_heapify(self, index):
        if self.is_leaf(index):
            return
        l = self.left(index)
        r = self.right(index)
        if l <= self.heap_size and self.heap[l] > self.heap[index]:
            largest = l
        else:
            largest = index
        if r <= self.heap_size and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != index:
            self.swap(index, largest)
            self.max_heapify(largest)

    def insert(self, item):
        if self.is_full():
            print("Heap is full...")
            return
        self.current_position = self.current_position + 1
        self.heap[self.current_position] = item
        current = self.current_position
        while self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def extract_max(self):
        if self.current_position == -1:
            return None
        popped = self.heap[0]
        self.swap(0, self.current_position)
        self.current_position = self.current_position - 1
        self.max_heapify(0)

    def delete(self, index):
        self.swap(index, self.current_position)
        self.current_position = self.current_position - 1
        self.max_heapify(index)

    def heap_sort(self):
        len = self.current_position
        i = 0
        while self.current_position > 1:
            self.delete(i)
            i = i + 1
        for i in range(0, len):
            print(self.heap[i])
