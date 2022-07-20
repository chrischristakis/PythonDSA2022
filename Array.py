class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, i):
        return self.data[i]

    def add(self, val):
        self.data[self.length] = val;
        self.length += 1

    def pop(self):
        popped = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return popped

    def delete(self, index):
        deleted = self.data[self.length-1]
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1
        return deleted

    def __str__(self):
        return str(self.data)


x = Array()
x.add("1")
x.add("2")
x.add("3")
x.add("4")
print(x)