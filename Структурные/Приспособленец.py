"""
Позволяет снизить использование памяти и увеличить производительность, разделяя общую информацию между
множеством мелких объектов.
"""


class Flyweight:
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        s = f"Flyweight: Displaying shared ({self._shared_state}) and unique ({unique_state}) state."
        print(s)


class FlyweightFactory:
    _flyweights = {}

    def __init__(self, initial_flyweights):
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state):
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state):
        key = self.get_key(shared_state)

        if key not in self._flyweights:
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self):
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("n".join(map(str, self._flyweights.values())))


# Пример использования
if __name__ == "__main__":
    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    flyweight1 = factory.get_flyweight(["BMW", "X6", "white"])
    flyweight1.operation("1234")

    flyweight2 = factory.get_flyweight(["Mercedes Benz", "C300", "black"])
    flyweight2.operation("4567")


"""
    Этот код показывает, как паттерн Приспособленец может использоваться для экономии памяти при работе с множеством 
объектов, имеющих общие свойства. В данном случае, мы создаем несколько объектов класса Flyweight, каждый из которых 
имеет общее состояние и уникальное состояние. Класс FlyweightFactory отвечает за создание и хранение объектов Flyweight, 
а также за их повторное использование, если объект с заданным состоянием уже существует.
"""