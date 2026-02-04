ArraySize = 7

class BucketNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Bucket:
    def __init__(self):
        self.head = None

    def insert(self, key: str, value: int) -> None:
        current = self.head
        # Ищем, существует ли ключ
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        # Ключ не найден — вставляем новый узел в начало
        new_node = BucketNode(key, value)
        new_node.next = self.head
        self.head = new_node


    def search(self, key: str) -> int:
        current_node = self.head
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        return 0

    def remove(self, key: str) -> None:
        if self.head is None:
            return

        if self.head.key == key:
            self.head = self.head.next
            return

        prev_node = self.head
        current_node = self.head.next

        while current_node is not None:
            if current_node.key == key:
                prev_node.next = current_node.next
                return

            prev_node = current_node
            current_node = current_node.next


def _hash(key: str) -> int:
    sum = 0
    for char in key:
        sum += ord(char)
    return sum % ArraySize


class HashTable:
    def __init__(self):
        self.array = [Bucket() for _ in range(ArraySize)]

    def insert(self, key: str, value: int) -> None:
        index = _hash(key)
        self.array[index].insert(key, value)

    def search(self, key: str) -> int:
        index = _hash(key)
        return self.array[index].search(key)

    def remove(self, key: str) -> None:
        index = _hash(key)
        self.array[index].remove(key)


ht = HashTable()
for i in range(len(ht.array)):
    ht.array[i] = Bucket()

print("Hash Table created")
ht.insert("name", 123)
ht.insert("age", 234)

name = ht.search("name")
age = ht.search("age")

print(f"name: {name}, age: {age}")
ht.remove("name")

name = ht.search("name")
print(f"name: {name}")

