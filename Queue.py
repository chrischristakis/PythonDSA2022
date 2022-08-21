class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Queue:
    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None

    def peek(self):
        return self.first.data

    def enqueue(self, val):
        newnode = Node(val)
        if self.size == 0:
            self.first = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None

        if self.first is self.last:
            self.last = None

        popped = self.first
        self.first = popped.next
        self.size -= 1

    def print_queue(self):
        temp = []
        curr = self.first
        while curr:
            temp.append(curr.data)
            curr = curr.next
        print(temp)
        print("First:", self.first.data)
        print("Last:", self.last.data)


queue = Queue()
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(6)
print(queue.peek())
queue.print_queue()
queue.dequeue()
queue.print_queue()