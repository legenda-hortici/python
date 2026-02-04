class Queue:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

    def is_empty(self):
        return self.data == []

    def print(self):
        return self.data

q = Queue()
for i in range(1, 6):
    q.push(i)

q.push(6)
q.push(7)
print(q.pop()) # 1
print(q.peek()) # 2
print(q.is_empty()) # False
print(q.print()) # [2, 3, 4, 5, 6, 7]