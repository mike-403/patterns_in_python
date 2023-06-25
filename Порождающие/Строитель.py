"""
Позволяет создавать сложные объекты пошагово, избегая конструкторов со многими параметрами.
"""


class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.engine = None
        self.transmission = None
        self.color = None


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_make(self, make):
        self.car.make = make

    def set_model(self, model):
        self.car.model = model

    def set_year(self, year):
        self.car.year = year

    def set_engine(self, engine):
        self.car.engine = engine

    def set_transmission(self, transmission):
        self.car.transmission = transmission

    def set_color(self, color):
        self.car.color = color

    def get_car(self):
        return self.car


class CarDirector:
    def __init__(self, builder):
        self._builder = builder

    def construct_car(self, make, model, year, engine, transmission, color):
        self._builder.set_make(make)
        self._builder.set_model(model)
        self._builder.set_year(year)
        self._builder.set_engine(engine)
        self._builder.set_transmission(transmission)
        self._builder.set_color(color)
        return self._builder.get_car()


# Пример использования
# Создаем строителя
builder = CarBuilder()

# Создаем директора и передаем ему строителя
director = CarDirector(builder)

# Строим объект автомобиля
car = director.construct_car('Mercedes', 'S-Class', 2021, 'V6', 'Automatic', 'Black')

# Выводим информацию об автомобиле
print(car.make, car.model, car.year, car.engine, car.transmission, car.color)


"""
    В этом примере мы создали класс Car, который представляет объект, который мы хотим создать. Затем мы создали класс 
CarBuilder, который содержит методы для пошагового создания объекта Car. Затем мы создали класс CarDirector, который 
используется для управления процессом построения объекта Car.

    Мы создали экземпляр builder класса CarBuilder, затем передали его в конструктор CarDirector. Затем мы вызвали метод 
construct_car() у director, передав ему необходимые параметры для создания объекта Car.

    В результате мы получили объект car, который содержит все параметры, которые мы задали при построении.
"""