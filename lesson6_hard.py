class Factory:

    def __init__(self, color = 'red', type = 'Toy'):
        self._material = 0
        self._name = 'Toy Factory №1'
        self._color = color
        self._type = type

    def buy_material(self, buy):
        self._material += int(buy)
        print(f'На завод поступило {buy} шт. сырья')

    def working(self):
        print('Происходит пошив игрушки...')

    def painting(self):
        print(f'Красим все в {self._color} цвет!')

    def finish(self):
        name = f'{self._name}'
        color = self._color
        if self._type == 'Toy':
            return Toy(name, color)
        if self._type == 'AnimalToy':
            return AnimalToy(name, color)
        else:
            return CartoonToy(name, color)


class Toy:

    def __init__(self, name, color):
        self.name = name
        self.color = color
    def say(self):
        print('Hello! I am just a toy')

class AnimalToy(Toy):

    def __init__(self, name, color, animal_type = 'Bear'):
        super().__init__(name, color)
        self.animal_type = animal_type
    def say(self):
        print(f'Hello! I am {self.animal_type} from {self.name} '
              f'and {self.color} colored')


class CartoonToy(Toy):

    def __init__(self, name, color, cartoon_hero = 'MickeyMouse'):
        super().__init__(name, color)
        self.cartoon_hero = cartoon_hero

    def say(self):
        print(f'Hello! I am {self.cartoon_hero} from {self.name} '
              f'and {self.color} colored')


#example

my_factory = Factory('blue', 'AnimalToy')
my_factory.buy_material(200)
my_factory.working()
my_factory.painting()
my_toy = my_factory.finish()
my_toy.say()