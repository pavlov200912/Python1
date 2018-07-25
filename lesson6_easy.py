class Car:
    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self, argument = 'Car'):
        print(f'{argument} поехала')
    def stop(self, argument):
        print(f'{argument} остановилась')