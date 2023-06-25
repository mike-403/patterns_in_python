"""
Позволяет передавать запросы последовательно по цепочке обработчиков, пока один из них не обработает запрос.
"""


class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        handled = self._handle(request)

        if not handled:
            self._successor.handle_request(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass.')


class ConcreteHandler1(Handler):
    def _handle(self, request):
        if 0 < request <= 10:
            print("Request {} handled in ConcreteHandler1".format(request))
            return True


class ConcreteHandler2(Handler):
    def _handle(self, request):
        if 10 < request <= 20:
            print("Request {} handled in ConcreteHandler2".format(request))
            return True


class ConcreteHandler3(Handler):
    def _handle(self, request):
        if 20 < request <= 30:
            print("Request {} handled in ConcreteHandler3".format(request))
            return True


class DefaultHandler(Handler):
    def _handle(self, request):
        print("End of chain, no handler for {}".format(request))
        return True


class Client:
    def __init__(self):
        self.handler = ConcreteHandler1(ConcreteHandler2(ConcreteHandler3(DefaultHandler())))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle_request(request)


# Пример использования:
if __name__ == "__main__":
    client = Client()
    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    client.delegate(requests)


"""
В данном примере мы создаем абстрактный класс Handler, который содержит метод handle_request(). 
Классы ConcreteHandler1, ConcreteHandler2, и ConcreteHandler3 наследуются от Handler и реализуют метод _handle(), 
который обрабатывает запросы в соответствии с определенными критериями. 

Мы также создаем класс DefaultHandler, который наследуется от Handler и используется в качестве последнего звена в 
цепочке обработчиков. 

В классе Client мы создаем объекты всех обработчиков и устанавливаем их в цепочку обработчиков в нужном порядке. 

В функции main() мы создаем объект Client и список запросов. Затем мы вызываем метод delegate(), чтобы передать запросы 
по цепочке обработчиков. Если ни один из обработчиков не может обработать запрос, то запрос передается на обработку в 
DefaultHandler.

Это пример простой цепочки обязанностей, который демонстрирует паттерн Цепочка обязанностей. Обработчики могут быть 
заменены на любые другие классы, которые могут обрабатывать запросы, а цепочка обработчиков может быть настроена в 
соответствии с конкретными требованиями.
"""