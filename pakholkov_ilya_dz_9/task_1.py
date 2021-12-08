import turtle
from time import sleep


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color == 'красный':
            turtle.dot(500, 'red')
            sleep(7)
            turtle.dot(500, 'yellow')
            sleep(2)
            turtle.dot(500, 'green')
            sleep(5)
        else:
            raise ValueError('Для запуска метода атрибут color должен быть "красный"')


instance = TrafficLight('красный')
instance.running()
