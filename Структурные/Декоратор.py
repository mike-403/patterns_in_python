"""
Позволяет добавлять новую функциональность объекту, не изменяя его класс.
"""


class Component:
    """
    Базовый класс Компонент объявляет общие операции как для простых, так и для
    декорированных объектов.
    """

    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    """
    Конкретный Компонент предоставляет реализацию базовых операций. Он может
    иметь некоторое поведение, которое может быть изменено декораторами.
    """

    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    """
    Базовый класс Декоратора следует тому же интерфейсу, что и другие
    компоненты. Основная цель этого класса - определить интерфейс обёртки для
    всех конкретных декораторов. Реализация кода обёртки по умолчанию может
    включать в себя поле для хранения завёрнутого компонента и средства его
    инициализации.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> str:
        """
        Декоратор делегирует всю работу обёрнутому компоненту.
        """

        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """
    Конкретные Декораторы вызывают обёрнутый объект и изменяют его результат
    некоторым образом.
    """

    def operation(self) -> str:
        """
        Декораторы могут вызывать родительскую реализацию операции, вместо
        того, чтобы вызвать обёрнутый объект напрямую. Такой подход упрощает
        расширение классов декораторов.
        """

        return f"ConcreteDecoratorA({self.component})"


class ConcreteDecoratorB(Decorator):
    """
    Декораторы могут выполнять своё поведение до или после вызова обёрнутого
    объекта.
    """

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component})"


"""
В этом примере Component определяет базовый интерфейс для всех компонентов. ConcreteComponent реализует этот интерфейс.

Decorator - базовый класс декоратора, который имеет ссылку на компонент, который он оборачивает. Метод operation у 
декоратора делегируется оборачиваемому компоненту.

ConcreteDecoratorA и ConcreteDecoratorB - конкретные декораторы, которые добавляют свою функциональность к компоненту.

Вот как можно использовать эти классы:
"""

def client_code(component: Component) -> None:
    """
    Клиентский код работает со всеми объектами, используя интерфейс Компонента.
    Таким образом, он остаётся независимым от конкретных классов компонентов,
    с которыми работает.
    """

    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":
    # Таким образом, клиентский код может поддерживать как простые компоненты...
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("n")

    # ...так и декорированные.
    #
    # Обратите внимание, что декораторы могут обёртывать не только простые
    # компоненты, но и другие декораторы.
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)
    print("n")


"""
Этот код создает простой компонент ConcreteComponent, а затем оборачивает его двумя декораторами ConcreteDecoratorA и 
ConcreteDecoratorB. Клиентский код работает с объектами через интерфейс Component, что позволяет ему работать как с 
простыми компонентами, так и с декорированными.
"""