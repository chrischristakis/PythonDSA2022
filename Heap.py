class MaxHeap:
    def __init__(self):
        self.arr = []
        self.size = 0

    def heapify(self, index):
        if self.size == 0:
            return

        largest = index
        l_index = 2 * index + 1  # left child
        r_index = 2 * index + 2  # right child

        # Find the largest of parent, r and l and set it to largest.
        if l_index < self.size and self.arr[l_index] > self.arr[largest]:
            largest = l_index

        if r_index < self.size and self.arr[r_index] > self.arr[largest]:
            largest = r_index

        # If a swap occurred, we must swap the nodes and heapify the subtrees recursively
        if largest != index:
            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
            self.heapify(largest)

    # Used when we want to heapify an existing array.
    def build_heap(self, arr):
        self.arr = arr
        self.size = len(arr)

        # We must get the last non leaf node, and start heapifying from there.
        last_non_leaf_index = (self.size // 2) - 1

        for i in range(last_non_leaf_index, -1, -1):
            self.heapify(i)

    def insert(self, val):
        self.arr.append(val)
        self.size += 1

        # We must now bubble this change through each node and check
        last_non_leaf_index = (self.size // 2) - 1
        for i in range(last_non_leaf_index, -1, -1):
            self.heapify(i)

    # Deletion is just putting node to back of array and swapping it last, then heapifying.
    def delete(self, val):
        if self.size == 0:
            return

        index = -1
        for i in range(0, self.size):
            if self.arr[i] == val:
                index = i
                break
        if index == -1:
            return

        self.arr[index], self.arr[self.size - 1] = self.arr[self.size - 1], self.arr[index]
        self.arr.pop()
        self.size -= 1

        last_non_leaf_index = (self.size // 2) - 1
        for i in range(last_non_leaf_index, -1, -1):
            self.heapify(i)

    def __str__(self):
        return str(self.__dict__)


testarr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
heap = MaxHeap()
heap.build_heap(testarr)
heap.insert(101)
heap.delete(6)
print(heap)
