class Node:
    def __init__(self, val=0, next=None):
        self.data = val
        self.next = next

# Our list will store a head, tail, and a length
class LinkedList:
    def __init__(self, val):
        node = Node(val)
        self.head = node
        self.tail = self.head
        self.length = 1

    # O(1)
    def append(self, val):
        newtail = Node(val)
        self.tail.next = newtail
        self.tail = newtail
        self.length += 1

    # O(1)
    def prepend(self, val):
        newhead = Node(val)
        newhead.next = self.head
        self.head = newhead
        self.length += 1

    # O(n)
    def insert(self, index, val):
        # Edge case, if index = 0, we'll have to just use our prepend method.
        if index == 0:
            return self.prepend(val)

        if index >= self.length:
            return self.append(val)

        # Traverse to is O(n), the rest is O(1) obviously.
        leader = self.traverse_to(index-1)
        newnode = Node(val)
        newnode.next = leader.next
        leader.next = newnode
        self.length += 1

    # O(n)
    def delete(self, index):
        # Edge case if index = 0, we cant use traverse_to(index-1). So just replace head.
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:  # If we removed the only element, head will be none so tail must be none too.
                self.tail = None
            return

        neighbour = self.traverse_to(index-1)
        to_delete = neighbour.next
        neighbour.next = to_delete.next

        # If we just deleted the last node, we must update the tail.
        if neighbour.next is None:
            self.tail = neighbour

        self.length -= 1

    def traverse_to(self, index):
        count = 0
        current_node = self.head
        while count != index:
            current_node = current_node.next
            count += 1
        return current_node

    def print_list(self):
        node = self.head
        temp = []
        while node:
            temp.append(node.data)
            node = node.next
        print(temp)
        print("Head:", self.head.data)
        print("Tail:", self.tail.data)
        print("Length:", self.length)

    def reverse(self):
        curr = self.head
        self.tail = curr
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev


llist = LinkedList(8)
llist.append(5)
llist.append(3)
llist.prepend(10)
llist.insert(2, 11)
llist.insert(99, 2)
llist.print_list()
llist.delete(5)
llist.delete(2)
llist.print_list()
llist.reverse()
llist.print_list()