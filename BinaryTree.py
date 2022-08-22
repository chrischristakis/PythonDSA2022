class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        curr = self.root
        while True:
            if val < curr.value:
                if curr.left is None:
                    curr.left = Node(val)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(val)
                    break
                curr = curr.right

    def lookup(self, val):
        if self.root is None:
            return None

        curr = self.root
        while curr:
            if val < curr.value:
                curr = curr.left
            elif val > curr.value:
                curr = curr.right
            else:
                return str(curr.__dict__)

        return None


# IGNORE FOR NOW
def print_tree(root):
    quene = []
    quene.append(root)
    while len(quene) != 0 :
        node = quene[0]
        if node.left is None:
            ll = '-'
        else:
            ll = node.left.value
        if node.right is None:
            rr = '-'
        else:
            rr = node.right.value
        print('  {n}  \n _|_ \n|   |\n{l}   {r}\n==========='.format(n = node.value, l = ll, r = rr))
        quene.pop(0)
        if node.left is not None:
            quene.append(node.left)
        if node.right is not None:
            quene.append(node.right)
    print('\n')


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(20)
tree.insert(1)
tree.insert(6)
tree.insert(170)
tree.insert(15)
print_tree(tree.root)
print(tree.lookup(9))
