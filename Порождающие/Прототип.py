"""
Позволяет создавать новые объекты, копируя существующие объекты, вместо того, чтобы создавать их заново.
"""


import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Регистрирует объект"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Удаляет объект"""
        del self._objects[name]

    def clone(self, name, **kwargs):
        """Клонирует объект"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(kwargs)
        return obj


class Car:
    def __init__(self):
        self.name = None
        self.color = None
        self.price = None

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.price)


# Пример использования
car = Car()
car.name = 'Mercedes'
car.color = 'Black'
car.price = 100000

prototype = Prototype()
prototype.register_object('car', car)

# Создаем копию объекта
car_copy = prototype.clone('car')

print(car_copy) # Mercedes | Black | 100000


"""
    В этом примере мы создали класс Prototype, который содержит словарь _objects для регистрации и хранения объектов. 
Метод clone() использует метод deepcopy() для создания глубокой копии объекта и обновляет его атрибуты, если были 
переданы дополнительные параметры. 

    Затем мы создали класс Car, который используется в качестве прототипа. Мы создали объект car и зарегистрировали его в 
экземпляре prototype. Затем мы создали копию объекта car с помощью метода clone() и вывели ее атрибуты.
"""