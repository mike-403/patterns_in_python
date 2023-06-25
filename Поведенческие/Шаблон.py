"""
Позволяет определить скелет алгоритма, перекладывая ответственность за некоторые его шаги на подклассы.
"""

from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self):
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        self.hook1()
        self.required_operation2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self):
        print("AbstractClass says: I am doing the bulk of the work here")

    def base_operation2(self):
        print("AbstractClass says: But I let subclasses override some operations")

    def base_operation3(self):
        print("AbstractClass says: But I am doing the bulk of the remaining work here")

    @abstractmethod
    def required_operation1(self):
        pass

    @abstractmethod
    def required_operation2(self):
        pass

    def hook1(self):
        pass

    def hook2(self):
        pass


class ConcreteClass1(AbstractClass):
    def required_operation1(self):
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operation2(self):
        print("ConcreteClass1 says: Implemented Operation2")


class ConcreteClass2(AbstractClass):
    def required_operation1(self):
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operation2(self):
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self):
        print("ConcreteClass2 says: Overridden Hook1")


"""
    В этом примере кода мы имеем абстрактный класс AbstractClass, который определяет основной шаблон выполнения 
определенной задачи с использованием методов template_method, base_operation1, base_operation2, base_operation3, 
required_operation1, required_operation2, hook1, и hook2. Класс AbstractClass содержит абстрактные методы 
required_operation1 и required_operation2, которые должны быть реализованы в конкретных подклассах.

    Конкретные классы ConcreteClass1 и ConcreteClass2 наследуются от AbstractClass и реализуют абстрактные методы 
required_operation1 и required_operation2. Класс ConcreteClass2 также переопределяет метод hook1.

    Клиентский код может создавать объекты конкретных классов и вызывать их методы template_method, которые реализуют 
определенный шаблон выполнения задачи.
"""