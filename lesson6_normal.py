class Person:

    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def _count_damage(self, person):
        return self.damage * (1 - min(1, person.armor))

    def attack(self, person):
        person.health = max(0, person.health - self._count_damage(person))


class Player(Person):

    def say(self):
        return 'Player'

    def attack(self, person):
        super().attack(person)
        print(f'Ha! Player hits!')


class Enemy(Person):

    def say(self):
        return 'Enemy'

    def attack(self, person):
        super().attack(person)
        print('Ouch! Enemy attack')


turn = True

l = input('Введите здоровье, урон и броню игрока:').split()
player = Player(int(l[0]), int(l[1]), float(l[2]))

l = input('Введите здоровье, урон и броню противника:').split()
enemy = Enemy(int(l[0]), int(l[1]), float(l[2]))

while True:
    person1 = player
    person2 = enemy

    if not turn:
        person1, person2 = person2, person1

    person1.attack(person2)
    turn = turn ^ 1

    if person2.health == 0:
        print(f'Game Over! {person1.say()} win!')
        break;
    else:
        print(f'{person2.say()} health is {person2.health}')
