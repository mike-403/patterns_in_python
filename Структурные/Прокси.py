"""
Позволяет контролировать доступ к объекту, добавляя дополнительную логику при его использовании.
"""


class Subject:
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")


class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")


# Пример использования
if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    proxy.request()


"""
    Концепция паттерна Прокси заключается в том, чтобы создать объект-заместитель, который может выступать в качестве 
замены другого объекта и контролировать доступ к нему.

    В этом примере Subject - это абстрактный класс, который определяет интерфейс для реального объекта и заместителя. 
RealSubject - это реальный объект, который выполняет основную функциональность. Proxy - это заместитель, который 
контролирует доступ к RealSubject.

    В методе request заместитель проверяет доступ к RealSubject, вызывает метод request реального объекта, если доступ 
разрешен, и затем регистрирует время запроса.

    Заместитель проверяет доступ к реальному объекту и вызывает его метод request. После выполнения запроса заместитель 
регистрирует время запроса.
"""