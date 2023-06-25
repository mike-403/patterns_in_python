"""
Позволяет уменьшить связанность между объектами, вынося взаимодействие между ними в отдельный объект-посредник.
"""


class Mediator:
    def __init__(self):
        self.colleague1 = Colleague1(self)
        self.colleague2 = Colleague2(self)

    def send_message(self, message, colleague):
        if colleague == self.colleague1:
            self.colleague2.receive_message(message)
        else:
            self.colleague1.receive_message(message)


class Colleague1:
    def __init__(self, mediator):
        self.mediator = mediator

    def send_message(self, message):
        self.mediator.send_message(message, self)

    def receive_message(self, message):
        print(f"Colleague1 received message: {message}")


class Colleague2:
    def __init__(self, mediator):
        self.mediator = mediator

    def send_message(self, message):
        self.mediator.send_message(message, self)

    def receive_message(self, message):
        print(f"Colleague2 received message: {message}")


# Пример использования:
mediator = Mediator()
mediator.colleague1.send_message("Hello, Colleague2!") # Output: Colleague2 received message: Hello, Colleague2!
mediator.colleague2.send_message("Hi, Colleague1!") # Output: Colleague1 received message: Hi, Colleague1!


"""
    В этом примере Mediator - это класс, который представляет посредника, который управляет взаимодействием между 
    объектами Colleague1 и Colleague2. Когда один из коллег отправляет сообщение через метод send_message(), посредник 
    пересылает это сообщение другому коллеге через его метод receive_message().

    Colleague1 и Colleague2 - это конкретные классы коллег, которые могут взаимодействовать друг с другом только через 
посредника.

    Когда объект Colleague1 отправляет сообщение через метод send_message(), посредник пересылает это сообщение объекту 
Colleague2 через его метод receive_message(). Аналогично, когда объект Colleague2 отправляет сообщение через метод 
send_message(), посредник пересылает это сообщение объекту Colleague1 через его метод receive_message().

    Таким образом, паттерн "Посредник" позволяет уменьшить связанность между объектами, позволяя им взаимодействовать 
друг с другом через объект-посредник.
"""