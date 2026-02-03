class Shop:
    # Базовый класс, представляющий товар в магазине
    def __init__(self, name, price):
        # super().__init__() — вызывает __init__ следующего класса в цепочке MRO
        super().__init__()
        print("init Shop")
        # Устанавливаем атрибуты экземпляра: название и цена
        self.name = name
        self.price = price

    def print_info(self):
        # Метод для вывода информации о товаре
        print(f"{self.name}, {self.price}")

class MixinLog:
    # Класс-миксин, добавляющий функциональность логирования
    ID = 0  # Атрибут класса: счётчик ID для всех экземпляров

    def __init__(self):
        # Конструктор миксина: увеличивает счётчик и присваивает ID
        print("init MixinLog")
        MixinLog.ID += 1  # Увеличиваем ID для следующего экземпляра
        self.id = MixinLog.ID  # Присваиваем текущий ID этому экземпляру

    def save_sell_log(self):
        # Метод для логирования продажи товара
        print(f"{self.id} товар был продан в 00:00 часов")

class NoteBook(Shop, MixinLog):
    # Класс, использующий множественное наследование
    # Наследуется от Shop и MixinLog
    pass

# Создаём экземпляр класса NoteBook
s = NoteBook('macbook', 100_000)
# При создании вызывается __init__ в порядке, определённом MRO:
# 1. NoteBook.__init__ (не определён, но цепочка начинается с Shop.__init__)
# 2. Shop.__init__ (выводит "init Shop", устанавливает name и price)
# 3. super().__init__() в Shop вызывает MixinLog.__init__ (выводит "init MixinLog", устанавливает id)

s.print_info()  # Вызывает метод из класса Shop
s.save_sell_log()  # Вызывает метод из класса MixinLog

# Выводит порядок разрешения методов (Method Resolution Order)
print(NoteBook.__mro__)
# (<class '__main__.NoteBook'>, <class '__main__.Shop'>, <class '__main__.MixinLog'>, <class 'object'>)
# Это порядок, в котором Python ищет методы при вызове