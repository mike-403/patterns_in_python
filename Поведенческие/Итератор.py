"""
Предоставляет способ доступа к элементам коллекции без раскрытия ее внутренней структуры.
"""


class MyList:
    def __init__(self):
        self.items = []

    def add(self, value):
        self.items.append(value)

    def __iter__(self):
        return MyIterator(self)


class MyIterator:
    def __init__(self, my_list):
        self.my_list = my_list
        self.index = 0

    def __next__(self):
        if self.index < len(self.my_list.items):
            value = self.my_list.items[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


# Пример использования:
my_list = MyList()
my_list.add(1)
my_list.add(2)
my_list.add(3)

for item in my_list:
    print(item) # Выводит: 1 2 3


"""
    В этом примере мы создаем класс MyList, который представляет список элементов. Класс MyIterator - это наш итератор, 
который будет перебирать элементы списка. 

    Метод __iter__ возвращает экземпляр MyIterator, который будет использоваться для перебора элементов списка. 

    Метод __next__ возвращает следующий элемент списка, или возбуждает исключение StopIteration, если больше элементов 
нет. 

    В примере мы создаем экземпляр MyList, добавляем в него несколько элементов и затем перебираем их в цикле for. 

    Когда мы вызываем for item in my_list:, интерпретатор Python вызывает метод __iter__ нашего объекта my_list, который 
возвращает экземпляр MyIterator. Затем интерпретатор Python вызывает метод __next__ нашего итератора, чтобы получить 
первый элемент списка. Этот процесс продолжается до тех пор, пока не будут перебраны все элементы списка.
"""