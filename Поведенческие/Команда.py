"""
Инкапсулирует запросы в виде объектов, позволяя откладывать выполнение команд, ставить их в очередь, логировать их,
а также поддерживать отмену операций.
"""


class Command:
    def execute(self):
        pass


class Light:
    def on(self):
        print("Свет включен")

    def off(self):
        print("Свет выключен")


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


class RemoteControl:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def press_button(self, index):
        self.commands[index].execute()


# Пример использования:
light = Light()
light_on_command = LightOnCommand(light)
light_off_command = LightOffCommand(light)

remote_control = RemoteControl()
remote_control.add_command(light_on_command)
remote_control.add_command(light_off_command)

remote_control.press_button(0) # Включает свет
remote_control.press_button(1) # Выключает свет


"""
    В этом примере мы создаем класс Command, который представляет команду, которую можно выполнить. Далее мы создаем 
класс Light, который представляет собой объект, над которым можно выполнять команды. 

    Затем мы создаем два класса LightOnCommand и LightOffCommand, которые представляют команды включения и выключения 
света. Каждый из них принимает экземпляр Light в качестве параметра в конструкторе, чтобы знать, над каким объектом 
выполнять команду. 

    Мы также создаем класс RemoteControl, который представляет пульт дистанционного управления. Он имеет список команд, 
которые можно добавить, и метод press_button, который принимает индекс команды и вызывает ее метод execute. 

    В примере мы создаем экземпляр Light, создаем команды включения и выключения света, добавляем их в пульт 
дистанционного управления и затем вызываем их методы execute, используя метод press_button нашего пульта 
дистанционного управления.
"""