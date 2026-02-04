class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def contains(self, value):
        last = self.head
        while last:
            if last.key == value:
                return True
            else:
                last = last.next

        return False

    def insert(self, value) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def get(self, index) -> int:
        last = self.head
        node_index = 0
        while node_index <= index:
            if node_index == index:
                return last.value
            node_index += 1
            last = last.next

        return -1


    def remove(self, value) -> None:
        current = self.head

        # Если голова содержит искомое значение
        if current and current.value == value:
            self.head = current.next
            return

        # Ищем узел, который нужно удалить
        prev = None
        while current:
            if current.value == value:
                break
            prev = current
            current = current.next

        # Если значение не найдено
        if current is None:
            return

        # Удаляем узел
        prev.next = current.next

    def print(self) -> None:
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)

ll.print() # 1 2 3 4

print(ll.get(2)) # 3

ll.remove(2)

ll.print() # 1 3 4
