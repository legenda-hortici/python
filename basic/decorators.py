"""
    Декораторы — это функции, которые модифицируют поведение других функций или классов.
    Они позволяют добавлять функциональность к существующему коду без изменения его тела.
    Декораторы — это один из важнейших механизмов в Python, широко используемый в фреймворках и библиотеках.
"""

"""
    1 - базовое определение декоратора
    2 - декоратор с аргументами
    3 - возврат значения из декорируемой функции
    4 - декораторы с параметрами
    5 - встроенные декораторы
    6 - functools.wraps
    7 - примеры полезных декораторов
    8 - декораторы классов
"""

### 1 - базовое определение декоратора
"""
    Декоратор — это функция, принимающая другую функцию и возвращающая новую функцию.
    Синтаксис: @имя_декоратора_перед_определением_функции.
"""
# Пример: простой декоратор
def my_decorator(func):
    def wrapper():
        print("Что-то выполняется до функции")
        func()
        print("Что-то выполняется после функции")
    return wrapper

@my_decorator
def say_hello():
    print("Привет!")

say_hello()

### 2 - декоратор с аргументами
"""
    Если декорируемая функция принимает аргументы, обёртка должна их принимать и передавать.
    Используются *args и **kwargs для универсального захвата аргументов.
"""
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print("До вызова функции")
        result = func(*args, **kwargs)
        print("После вызова функции")
        return result
    return wrapper

@decorator_with_args
def greet(name):
    print(f"Привет, {name}!")

greet("Алиса")

### 3 - возврат значения из декорируемой функции
"""
    Декоратор может возвращать результат декорируемой функции.
    Важно не забывать возвращать значение из wrapper.
"""
def return_decorator(func):
    def wrapper(*args, **kwargs):
        print("Выполняем до функции")
        result = func(*args, **kwargs)
        print("Выполняем после функции")
        return result
    return wrapper

@return_decorator
def add(a, b):
    return a + b

result = add(3, 5)
print(result) # 8

### 4 - декораторы с параметрами
"""
    Декоратор может принимать свои параметры.
    В этом случае нужна трёхуровневая вложенная функция.
"""
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
            return None
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Привет!")

hello() # "Привет!" напечатается 3 раза

### 5 - встроенные декораторы
"""
    Python предоставляет встроенные декораторы:
    - @property — позволяет обращаться к методу как к атрибуту
    - @staticmethod — делает метод статическим
    - @classmethod — делает метод методом класса
"""
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, int):
            self._value = new_value
        else:
            raise ValueError("Значение должно быть числом")

obj = MyClass(10)
print(obj.value) # 10
obj.value = 20
print(obj.value) # 20

### 6 - functools.wraps
"""
    При создании декораторов важно сохранять метаданные оригинальной функции.
    functools.wraps копирует name, doc и другие атрибуты.
"""
from functools import wraps

def my_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} выполнялась {end - start:.4f} секунд")
        return result
    return wrapper

@my_timer
def slow_function():
    import time
    time.sleep(1)

slow_function() # slow_function выполнялась ~1.0001 секунд

### 7 - примеры полезных декораторов
"""
    Примеры часто используемых декораторов:
    - логирование
    - кэширование
    - проверка аутентификации
    - ограничение частоты вызовов
"""
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} завершена")
        return result
    return wrapper

@log_calls
def multiply(x, y):
    return x * y

multiply(3, 4)

### 8 - декораторы классов
"""
Декораторы могут применяться и к классам, модифицируя их поведение.
"""
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Создаём подключение к БД")

db1 = Database() # Создаём подключение к БД
db2 = Database() # (ничего не выводится — тот же экземпляр)
print(db1 is db2) # True

"""
    Основные особенности декораторов:
    1. Позволяют модифицировать поведение функций и классов.
    2. Используют синтаксис @имя_декоратора.
    3. Могут принимать свои параметры.
    4. Используют вложенные функции для оборачивания.
    5. Используют functools.wraps для сохранения метаданных.
    6. Широко применяются в фреймворках и библиотеках.
    7. Позволяют писать чистый, переиспользуемый код.
"""