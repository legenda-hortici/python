from accessify import private, protected

class Point:
    def __init__(self, x):
        """
        Атрибуты с уровнем доступа public (публичные).
        Они доступны из любого места программы: внутри и вне класса.
        """
        self.attr_pub = x # attr_pub: public

        """
        Атрибуты с уровнем доступа protected (защищённые).
        Это соглашение: имя начинается с одного подчёркивания (_).
        Такие атрибуты предназначены для использования внутри класса и его наследников.
        Но Python не запрещает доступ к ним извне — это лишь сигнал программисту.
        """
        self._attr_prot = x # _attr_prot: protected

        """
        Атрибуты с уровнем доступа private (приватные).
        Это соглашение: имя начинается с двух подчёркиваний (__).
        Python применяет "name mangling": извне атрибут будет доступен как _Point__attr_prvt.
        Тем не менее, это тоже не настоящая защита — доступ возможен, но не рекомендован.
        """
        self.__attr_prvt = x # __attr_prvt: private

    """
    Метод, помеченный как private с помощью библиотеки accessify.
    Он не будет доступен извне, даже через объект или класс.
    """
    @private
    def check_value(self, value):  # заменил cls на self, т.к. это метод экземпляра
        return type(value) in (int, float)

pt = Point(1)

# Доступ к public атрибуту — разрешён
pt.attr_pub = 10
print(pt.attr_pub) # 10

# Доступ к protected атрибуту — разрешён, но не рекомендован
pt._attr_prot = 20
print(pt._attr_prot) # 20 (IDE может подсвечивать предупреждение)

# Попытка вызова private метода через библиотеку accessify — вызывает ошибку
# print(pt.check_value(10)) # вызовет исключение InaccessibleDueToItsProtectionLevelException

# Попытка присвоить значение новому атрибуту __attr_prvt — НЕ изменяет внутренний __attr_prvt!
pt.__attr_prvt = 30  # Это создаст новый атрибут в объекте, не связанный с __attr_prvt

# Попытка доступа к __attr_prvt вызывает ошибку, потому что реальный атрибут — _Point__attr_prvt
# print(pt.__attr_prvt) # AttributeError: 'Point' object has no attribute '__attr_prvt'