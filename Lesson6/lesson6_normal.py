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


class Fight:

    def __init__(self, fighter1, fighter2):
        self._fighter1 = fighter1
        self._fighter2 = fighter2


    def _fighter_attack(self, attacker, defender):
        attacker.attack(defender)


    def _game_status(self, at, de):
        if de.health == 0:
            print(f'Game over!{at.say()} win')
            return True
        else:
            print(f'{at.say()} attacked! {de.say()} has {de.health} health.')
            return False


    def start_fight(self):
        while True:
            self._fighter_attack(self._fighter1, self._fighter2)
            if self._game_status(self._fighter1, self._fighter2):
                break
            self._fighter1, self._fighter2 = self._fighter2, self._fighter1


l = input('Введите здоровье, урон и броню игрока:').split()
player = Player(int(l[0]), int(l[1]), float(l[2]))

l = input('Введите здоровье, урон и броню противника:').split()
enemy = Enemy(int(l[0]), int(l[1]), float(l[2]))

epic_figth = Fight(player, enemy)
epic_figth.start_fight()
