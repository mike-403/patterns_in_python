"""
Позволяет скрыть сложность системы за простым интерфейсом, упрощая ее использование.
"""


class Subsystem1:
    def operation1(self):
        print("Subsystem1 operation")


class Subsystem2:
    def operation2(self):
        print("Subsystem2 operation")


class Facade:
    def __init__(self):
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()

    def operation(self):
        self._subsystem1.operation1()
        self._subsystem2.operation2()


# Пример использования
facade = Facade()
facade.operation()


"""
    В этом примере мы создаем две подсистемы Subsystem1 и Subsystem2, каждая из которых выполняет свою операцию. 
Затем мы создаем класс Facade, который предоставляет упрощенный интерфейс для использования этих подсистем.

    Класс Facade инициализирует объекты Subsystem1 и Subsystem2 в своем конструкторе, а метод operation предоставляет 
упрощенный интерфейс для выполнения операций подсистем.

    При использовании фасада в нашем коде, мы создаем объект класса Facade и вызываем его метод operation, который в 
    свою очередь вызывает методы операций Subsystem1 и Subsystem2. Таким образом, мы можем использовать подсистемы, 
    не заботясь о деталях их реализации.
"""