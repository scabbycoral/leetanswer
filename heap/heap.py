class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def heapify(self, i, n):
    #单个节点的heapify
        #从位置i一直往孩子节点找，直到左右孩子都比当前节点小
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)
        #先找位置
        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        #再交换，并进行新位置的heapify
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]  # Swap
            self.heapify(largest, n)  # Recursively heapify the affected subtree

    def build_heap(self, arr):
    #从最后一个非叶节点到root的build
        self.heap = arr
        n = len(arr)
        # Start from the last non-leaf node and call heapify on each node
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i, n)
            print(self.heap)

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        # "Up-heap" or "bubble up" operation
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_max(self):
        if len(self.heap) < 1:
            raise IndexError("Heap underflow")

        max_val = self.heap[0]
        # Replace root with the last element
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        # "Down-heap" or "bubble down" operation
        self.heapify(0, len(self.heap))
        return max_val

    def get_max(self):
        if len(self.heap) < 1:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def display(self):
        print(self.heap)

# Example usage:
heap = MaxHeap()
arr = [4, 10, 3, 5, 1]
heap.build_heap(arr)
heap.display()  # Output: [10, 5, 3, 4, 1]

heap.insert(15)
heap.display()  # Output: [15, 10, 3, 5, 1, 4]

print(f"Extracted max: {heap.extract_max()}")  # Output: Extracted max: 15
heap.display()  # Output: [10, 5, 3, 4, 1]
