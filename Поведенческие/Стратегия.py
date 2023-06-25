"""
Определяет семейство алгоритмов, инкапсулирует каждый из них и делает их взаимозаменяемыми.
"""

from abc import ABC, abstractmethod


# Абстрактный класс стратегии
class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data):
        pass


# Конкретные классы стратегии
class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data):
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data):
        return reversed(sorted(data))


# Контекст
class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_some_business_logic(self, data):
        result = self._strategy.do_algorithm(data)
        return result


# Пример использования
data = [1, 5, 3, 2, 4]

strategy_a = ConcreteStrategyA()
context = Context(strategy_a)
result = context.do_some_business_logic(data)
print(result)

strategy_b = ConcreteStrategyB()
context.set_strategy(strategy_b)
result = context.do_some_business_logic(data)
print(result)


"""
    В этом примере мы создаем абстрактный класс Strategy, который определяет интерфейс для всех конкретных стратегий. 
Затем мы создаем две конкретные стратегии ConcreteStrategyA и ConcreteStrategyB, которые реализуют этот интерфейс.

    Далее мы создаем класс Context, который представляет контекст и имеет ссылку на объект Strategy. 
Метод do_some_business_logic вызывает метод do_algorithm объекта Strategy.

    При использовании стратегии в нашем коде, мы создаем объекты конкретных стратегий ConcreteStrategyA и ConcreteStrategyB, 
а затем передаем их в объект Context. Метод do_some_business_logic объекта Context вызывает метод do_algorithm 
соответствующего объекта Strategy, который возвращает результат обработки данных. Таким образом, мы можем использовать 
различные стратегии для обработки данных, не затрагивая код контекста.
"""