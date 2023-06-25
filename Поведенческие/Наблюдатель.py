"""
Определяет зависимость "один ко многим" между объектами таким образом, что при изменении состояния одного объекта все
зависимые от него объекты уведомляются и автоматически обновляются.
"""

class Observer:
    def update(self, observable, *args, **kwargs):
        pass


class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(self, *args, **kwargs)


class TemperatureSensor(Observable):
    def __init__(self):
        super().__init__()
        self.temperature = 0

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers(self.temperature)


class TemperatureDisplay(Observer):
    def update(self, observable, *args, **kwargs):
        if isinstance(observable, TemperatureSensor):
            temperature = kwargs.get('temperature')
            print(f"Temperature changed to {temperature}")


# Пример использования:
sensor = TemperatureSensor()
display = TemperatureDisplay()

sensor.add_observer(display)

sensor.set_temperature(25) # Output: Temperature changed to 25


"""
    В этом примере Observable - это класс, который представляет наблюдаемый объект, который может иметь несколько 
наблюдателей (Observer). Когда наблюдаемый объект изменяет свое состояние, он вызывает метод notify_observers(), чтобы 
оповестить всех своих наблюдателей.

    TemperatureSensor - это конкретный класс наблюдаемого объекта, который представляет датчик температуры. 
TemperatureDisplay - это конкретный класс наблюдателя, который представляет дисплей для отображения температуры.

    Когда объект TemperatureSensor изменяет свое состояние (температуру), он вызывает метод notify_observers() для 
оповещения всех своих наблюдателей. В этом примере у нас есть только один наблюдатель (TemperatureDisplay), который 
реализует метод update(), который выводит новую температуру на консоль.
"""