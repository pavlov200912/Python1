class Car:

    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'{type(self).__name__} поехала')

    def stop(self):
        print(f'{type(self).__name__} остановилась')

    def turn(self, direction):
        print(f'{type(self).__name__} повернула в направлении {direction}')


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    pass


# example
police = PoliceCar(120, 'red', 'Mustang', True)
police.go()
police.turn('налево')
police.stop()
