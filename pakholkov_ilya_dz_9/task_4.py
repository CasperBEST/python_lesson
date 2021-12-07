class Car:

    def __init__(self, speed, color, name, is_police=bool()):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'the car {self.name} started moving')

    def stop(self):
        print(f'the car {self.name} stopped')

    def turn(self, direction):
        print(f'the car {self.name} turned {direction}')

    def show_speed(self):
        print(f'Car speed {self.speed} km/h')


class TownCar(Car):

    def __init__(self, speed, color='yellow', name='taxi', is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Car speed {self.speed} km/h')
        if self.speed > 60:
            print(f'Warnind. Speed limit 60 km/h')


class SportCar(Car):

    def __init__(self, speed, color='red', name='targa', is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color='blue', name='bus', is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Car speed {self.speed} km/h')
        if self.speed > 40:
            print(f'Warnind. Speed limit 40 km/h')


class PoliceCar(Car):
    def __init__(self, speed, color='black', name='police', is_police=True):
        super().__init__(speed, color, name, is_police)


car_1 = TownCar(100, 'pink', 'trolleybus')
car_2 = SportCar(120)
car_3 = WorkCar(60)
car_4 = PoliceCar(90)

print(car_1.speed)
print(car_1.color)
print(car_1.name)
print(car_1.is_police)

print(car_2.speed)
print(car_2.color)
print(car_2.name)
print(car_2.is_police)

print(car_3.speed)
print(car_3.color)
print(car_3.name)
print(car_3.is_police)

print(car_4.speed)
print(car_4.color)
print(car_4.name)
print(car_4.is_police)

car_1.go()
car_1.turn('left')
car_1.show_speed()
car_1.speed = 60
car_1.show_speed()
car_1.stop()

car_2.go()
car_2.turn('right')
car_2.show_speed()
car_2.stop()

car_3.go()
car_3.turn('right')
car_3.show_speed()
car_3.speed = 40
car_3.show_speed()
car_3.stop()

car_4.go()
car_4.turn('left')
car_4.show_speed()
car_4.stop()
