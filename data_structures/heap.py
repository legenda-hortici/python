class MinHeap:
    def __init__(self):
        self.data = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, value):
        self.data.append(value)
        self._heapify_up(len(self.data) - 1)

    def swap(self, a, b):
        self.data[a], self.data[b] = self.data[b], self.data[a]

    def peek(self):
        if not self.data:
            raise IndexError("peek from empty heap")
        return self.data[0]

    def extract_min(self):
        if not self.data:
            raise IndexError("extract from empty heap")
        min_val = self.data[0]
        last_val = self.data.pop()
        if self.data:
            self.data[0] = last_val
            self._heapify_down(0)
        return min_val

    """
        _heapify_up(index):
        Сравнивает элемент с родителем.
        Если текущий элемент меньше родителя, они меняются местами.
        Процесс повторяется, пока куча не станет корректной.
    """
    def _heapify_up(self, index):
        while index > 0:
            parent_index = self.parent(index)
            if self.data[index] < self.data[parent_index]:
                self.swap(index, parent_index)
                index = parent_index
            else:
                break

    """
        _heapify_down(index):
        Сравнивает элемент с его потомками.
        Меняется местами с наименьшим потомком, если текущий больше него.
        Процесс продолжается, пока куча не станет корректной.
    """
    def _heapify_down(self, index):
        size = len(self.data)
        while True:
            smallest = index
            left = self.left_child(index)
            right = self.right_child(index)
            if left < size and self.data[left] < self.data[smallest]:
                smallest = left
            if right < size and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest != index:
                self.swap(smallest, index)
                index = smallest
            else:
                break

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0


h = MinHeap()
h.insert(3)
h.insert(1)
h.insert(4)
h.insert(2)

print(h.peek())  # 1
print(h.extract_min())  # 1
print(h.extract_min())  # 2
print(h.peek())  # 3
