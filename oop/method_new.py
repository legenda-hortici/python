class Point:
    """
    Параметр cls ссылается на сам класс Point
    """
    def __new__(cls, *args, **kwargs):
        print(f"Вызов __new__ для {str(cls)}")
        """
        super() это встроенная функция в базовом классе object с версии языка 3.x
        """
        return super().__new__(cls)

    """
    А параметр self ссылается на объект класса Point
    """
    def __init__(self, x = 0, y = 0):
        print(f"Вызов __init__ для {str(self)}")
        self.x = x
        self.y = y

pt = Point(1, 2) # Вызов __new__ для <class '__main__.Point'> | Вызов __init__ для <__main__.Point object at 0x105a92120>
"""
Был вызван только метод __new__, то есть объект класса не был создан,
но если вернуть ссылку на класс через метод super() от базового класса (object),
то мы можем создать объект класса
"""
# print(pt) # None - не вернули ссылку на класс
# print(pt) # <__main__.Point object at 0x105a92120> | Успешно создали объект класса Point

"""
При создании объекта сначала вызывается __new__ (он создаёт объект), при этом если он не объявлен в классе
то все равно будет вызван неявно, а затем __init__ (он инициализирует его атрибуты).
"""

"""
Частичная реализация паттерна Singleton для демонстрации работы метода __new__
"""
class DataBase:

    __instance = None # переменная для проверки экземпляра

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None: # делаем проверку на существование ранее созданного объекта
            cls.__instance = super().__new__(cls) # если он не был создан, то создаем его
        return cls.__instance # возвращаем созданный объект

    def __init__(self, user, password, port):
        self.user: str = user
        self.password: str = password
        self.port: int = port

    def connect(self):
        print(f"Подключение к базе данных: {self.user}, {self.password}, {self.port}")

    def disconnect(self):
        print("закрытие подключения к БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print("Записаны данные: ", data)

db = DataBase("user", "password", 80)
db2 = DataBase("user1", "1234", 40)
print(id(db), id(db2)) # 4388066304 4388066304 - адреса одинаковые, а значит db2 указывает на ранее созданный объект db