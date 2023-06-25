"""
Позволяет объектам менять свое поведение в зависимости от своего внутреннего состояния.
"""

from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def do_action(self, context):
        pass


class StartState(State):
    def do_action(self, context):
        print("Player is in start state")
        context.state = self


class StopState(State):
    def do_action(self, context):
        print("Player is in stop state")
        context.state = self


class Context:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state


# Пример использования:
if __name__ == "__main__":
    context = Context()

    start_state = StartState()
    start_state.do_action(context)
    print(context.get_state())

    stop_state = StopState()
    stop_state.do_action(context)
    print(context.get_state())


"""
    В данном примере мы создаем абстрактный класс State, который содержит абстрактный метод do_action(). 
Затем мы создаем два класса StartState и StopState, которые наследуются от State и реализуют метод do_action(). 

    Мы также создаем класс Context, который содержит ссылку на текущее состояние объекта. Метод set_state() используется 
для установки текущего состояния объекта, а метод get_state() используется для получения текущего состояния объекта.

    В функции main() мы создаем объект Context и два объекта StartState и StopState. Затем мы вызываем метод do_action() 
для каждого объекта состояния, чтобы изменить состояние объекта Context. В конце мы выводим текущее состояние объекта 
Context.

    Это пример простого конечного автомата, который демонстрирует паттерн Состояние. Классы StartState и StopState могут 
быть заменены на любые другие классы состояния, а класс Context может быть заменен на любой объект, который может иметь 
различные состояния.
"""