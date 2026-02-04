class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return self.data == []

st = Stack()
for i in range(5):
    st.push(i)

st.push(6)
st.push(7)
print(st.pop()) # 7
print(st.peek()) # 6
print(st.is_empty()) # False