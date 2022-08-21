# Stack made with a linked list

class Node:
    def __init__(self, val=0, next=None):
        self.data = val
        self.next = next

class LLStack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def push(self, val):
        newnode = Node(val)

        if self.size == 0:
            self.top = newnode
            self.bottom = newnode
        else:
            newnode.next = self.top
            self.top = newnode

        self.size += 1

    def pop(self):
        if self.size == 0:
            return None

        removed = self.top
        self.top = removed.next
        self.size -= 1
        return removed

    def peek(self):
        return self.top.data

    def print_stack(self):
        if self.size == 0:
            return print("[]")

        temp = []
        curr = self.top
        while curr:
            temp.append(curr.data)
            curr = curr.next
        print(str(temp))
        print("Top:", self.top.data)
        print("Bottom:", self.bottom.data)
        print("Size:", self.size)


# Array implementation
class ArrayStack:
    def __init__(self):
        self.data = []
        self.length = 0

    def push(self, val):
        self.data.append(val)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None

        popped = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return popped

    def peek(self):
        return self.data[self.length-1]

    def size(self):
        return self.length

    def print_stack(self):
        print(self.__dict__)


stack = ArrayStack()
stack.push(1)
stack.push(2)
stack.pop()
stack.push(4)
print(stack.peek())
stack.print_stack()