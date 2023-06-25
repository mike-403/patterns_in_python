"""
Позволяет создавать семейства связанных объектов, не привязываясь к конкретным классам этих объектов.
"""

from abc import ABC, abstractmethod


# Абстрактные классы для создания объектов
class AbstractProductA(ABC):
    @abstractmethod
    def do_something(self):
        pass


class AbstractProductB(ABC):
    @abstractmethod
    def do_something_else(self):
        pass


# Конкретные классы для создания объектов ProductA1, ProductA2, ProductB1, ProductB2
class ProductA1(AbstractProductA):
    def do_something(self):
        print("Product A1")


class ProductA2(AbstractProductA):
    def do_something(self):
        print("Product A2")


class ProductB1(AbstractProductB):
    def do_something_else(self):
        print("Product B1")


class ProductB2(AbstractProductB):
    def do_something_else(self):
        print("Product B2")


# Абстрактная фабрика
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


# Конкретные фабрики для создания объектов ProductA и ProductB
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ProductB2()

# Класс-клиент, который использует объекты, созданные фабрикой
class Client:
    def __init__(self, factory: AbstractFactory):
        self.product_a = factory.create_product_a()
        self.product_b = factory.create_product_b()

    def do_something(self):
        self.product_a.do_something()
        self.product_b.do_something_else()


# Пример использования
factory1 = ConcreteFactory1()
client1 = Client(factory1)
client1.do_something()

factory2 = ConcreteFactory2()
client2 = Client(factory2)
client2.do_something()


"""
    В этом примере мы создаем абстрактные классы AbstractProductA и AbstractProductB, которые определяют интерфейсы 
для создания объектов ProductA и ProductB. Затем мы создаем конкретные классы ProductA1, ProductA2, ProductB1 и 
ProductB2, которые реализуют эти интерфейсы.

    Далее мы создаем абстрактную фабрику AbstractFactory, которая определяет интерфейсы для создания объектов ProductA и 
ProductB. Затем мы создаем две конкретные фабрики ConcreteFactory1 и ConcreteFactory2, которые реализуют эти интерфейсы.

    Наконец, мы создаем класс-клиент Client, который использует объекты, созданные фабрикой, и создаем двух клиентов 
client1 и client2, использующих соответствующие фабрики.
"""