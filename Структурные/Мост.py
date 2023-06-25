"""
Разделяет абстракцию и реализацию, позволяя им изменяться независимо друг от друга.
"""


from abc import ABC, abstractmethod


# Абстракция
class Abstraction:
    def __init__(self, implementation):
        self._implementation = implementation

    def operation(self):
        return f"Abstraction: {self._implementation.operation_implementation()}"


# Реализация
class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self):
        pass


# Конкретные реализации
class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA"


class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationB"


# Пример использования
implementation_a = ConcreteImplementationA()
abstraction = Abstraction(implementation_a)
print(abstraction.operation())

implementation_b = ConcreteImplementationB()
abstraction = Abstraction(implementation_b)
print(abstraction.operation())


"""
    В этом примере мы создаем класс Abstraction, который представляет абстракцию и имеет ссылку на объект 
Implementation. Метод operation вызывает метод operation_implementation объекта Implementation.

    Затем мы создаем абстрактный класс Implementation, который определяет интерфейс для всех конкретных реализаций. 
Мы создаем две конкретные реализации ConcreteImplementationA и ConcreteImplementationB, которые реализуют этот 
интерфейс.

    При использовании моста в нашем коде, мы создаем объекты конкретных реализаций ConcreteImplementationA и 
ConcreteImplementationB, а затем передаем их в объект Abstraction. Метод operation объекта Abstraction вызывает метод 
operation_implementation соответствующего объекта Implementation, который возвращает строку с именем конкретной 
реализации. Таким образом, мы можем использовать различные реализации, не затрагивая код абстракции.
"""