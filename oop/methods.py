class Point:
    color = "green"
    size = 2

    """
    set_fields() это метод класса Point. Параметр self нужен для того, чтобы
    ссылаться на объект, метод которого был вызван или обращаться к полям. 
    То есть это нужно, чтобы Point понимал какой конкретно объект вызвал его метод. 
    Методы также являются атрибутами класса
    """
    def set_fields(self, x, y):
        self.x = x
        self.y = y

    """
    get_fields() это так же метод класса Point
    """
    def get_fields(self):
        return self.x, self.y

pt = Point()
pt.set_fields(10, 20) # При вызове передается ссылка на объект и параметры
print(pt.get_fields()) # 10 20


