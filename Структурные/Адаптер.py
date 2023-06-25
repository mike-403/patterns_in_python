"""
Позволяет объектам работать вместе, несмотря на несовместимые интерфейсы.
"""


# Адаптируемый класс
class Adaptee:
    def specific_request(self) -> str:
        return "Интерфейс адаптируемого класса"


# Целевой интерфейс
class Target:
    def request(self) -> str:
        return "Целевой интерфейс"


# Адаптер
class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Адаптер: (TRANSLATED) {self.adaptee.specific_request()}"


# Клиентский код
def client_code(target: Target) -> None:
    print(target.request(), end="")


# Пример использования
if __name__ == "__main__":
    adaptee = Adaptee()
    print("Клиентский код работает с классом Adaptee:")
    print(adaptee.specific_request(), end="nn")

    target = Target()
    print("Клиентский код работает с целевым интерфейсом:")
    client_code(target)
    print("n")

    adapter = Adapter(adaptee)
    print("Клиентский код работает с адаптером:")
    client_code(adapter)
    print("n")


"""
    В этом примере класс Adaptee - это адаптируемый класс, у которого есть метод specific_request. Класс Target - 
это целевой интерфейс, который определяет метод request. Класс Adapter - это адаптер, который принимает в конструкторе 
объект Adaptee и реализует метод request целевого интерфейса, используя метод specific_request адаптируемого класса.

    Клиентский код использует объекты Adaptee, Target и Adapter. Он сначала работает с объектом Adaptee, вызывая его 
метод specific_request. Затем он работает с объектом Target, вызывая его метод request. Наконец, он работает с объектом 
Adapter, вызывая его метод request, который использует метод specific_request объекта Adaptee через адаптер.
"""