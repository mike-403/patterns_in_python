"""
Определяет интерфейс для создания объектов, но позволяет подклассам выбирать классы, которые следует создавать.
"""


from abc import ABC, abstractmethod


# Абстрактный класс для создания продуктов
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Создан {product.operation()}"
        return result


# Конкретный класс для создания продукта "Продукт 1"
class ConcreteCreator1(Creator):
    def factory_method(self) -> "ConcreteProduct1":
        return ConcreteProduct1()


# Конкретный класс для создания продукта "Продукт 2"
class ConcreteCreator2(Creator):
    def factory_method(self) -> "ConcreteProduct2":
        return ConcreteProduct2()


# Абстрактный класс для продукта
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


# Конкретный класс для продукта "Продукт 1"
class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "Продукт 1"


# Конкретный класс для продукта "Продукт 2"
class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "Продукт 2"


# Клиентский код
def client_code(creator: Creator) -> None:
    print(f"Клиентский код работает с {creator.some_operation()}", end="")


# Пример использования
if __name__ == "__main__":
    print("Запуск клиентского кода с ConcreteCreator1")
    client_code(ConcreteCreator1())
    print("n")

    print("Запуск клиентского кода с ConcreteCreator2")
    client_code(ConcreteCreator2())


"""
    В этом примере класс Creator - это абстрактный класс, который определяет интерфейс для создания продуктов. 
Конкретные подклассы ConcreteCreator1 и ConcreteCreator2 реализуют метод factory_method, который создает конкретные 
продукты ConcreteProduct1 и ConcreteProduct2. Классы ConcreteProduct1 и ConcreteProduct2 - это конкретные продукты, 
которые реализуют абстрактный метод operation.

    Клиентский код использует объекты Creator для создания продуктов, используя метод some_operation. В зависимости от 
переданного объекта Creator он создает разные продукты.
"""