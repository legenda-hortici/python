class Point:
    """Класс определяющий точку на плоскости
    Point является пространством имен с атрибутами(полями) color и circle
    """
    color = "red"
    circle = 2

print(Point.color) # red
print(Point.circle) # 2

print(Point.__dict__) # {'__module__': '__main__', '__firstlineno__': 1, '__doc__': 'Класс определяющий точку на плоскости\nPoint является пространством имен с атрибутами(полями) color и circle\n', 'color': 'red', 'circle': 2, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>}
print(Point.__doc__) # Класс определяющий точку на плоскости # Point является пространством имен с атрибутами(полями) color и circle

a = Point() # Экземпляр(объект) класса Point
b = Point() # Экземпляр(объект) класса Point

"""
При создании объекта создается ссылка на класс от которого он образован
"""
print(a) # <__main__.Point object at 0x10441d400>

"""
У объекта класса можно задавать свои "локальные" поля и задавать им значение
при этом значение поле класса от которого образован объект остается неизменным
"""
a.color = "blue"
print(a.color) # blue
print(Point.color) # red

a.x = 1
a.y = 2

print(a.x, a.y) # 1 2

# print(Point.x) # AttributeError: type object 'Point' has no attribute 'x'

"""
Поля можно удалять из класса при помощи операторов del и delattr()
при этом у объектов класса это поле остается, если оно было переопределено.
Так у объекта b, после удаления поля color из Point, отсутствует так же свойство color,
однако у объекта a оно остается, так как было переопределено раннее
"""
del Point.color

# print(Point.color) # AttributeError: type object 'Point' has no attribute 'color'
print(a.color) # blue
# print(b.color) # AttributeError: 'Point' object has no attribute 'color'

"""
Проверка на содержание атрибутов
"""
print(hasattr(a, "color")) # True
print(hasattr(b, "color")) # False
print(hasattr(Point, "color")) # False

"""
Установка полей класса и его объекта
"""
setattr(Point, "color", "green")
print(Point.color) # green
print(b.color) # green

setattr(Point, "size", 10)
print(Point.size) # 10
print(b.size) # 10
print(a.size) # 10

"""
Получение значений полей класса
"""
print(getattr(Point, "size")) # 10
print(getattr(Point, "color")) # green
print(getattr(Point, "circle")) # 2

