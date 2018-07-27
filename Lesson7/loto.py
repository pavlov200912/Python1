import random



class Card:

    def __init__(self, type = 'Player'):
        self._list = [i for i in range(100)]
        self._type = type

    def _get_numbers(self):
        out = set()
        while len(out) < 5:
            index = random.randint(1, len(self._list)) - 1
            out.add(self._list[index])
            self._list.pop(index)
        return out

    def _get_bold(self):
        if self._type == 'Player':
            return '------ Ваша карточка -----', '-' * 26
        else:
            return '-- Карточка компьютера ---', '-' * 26

    def _get_string(self, list):

        list = [str(x) for x in list] # Вставляем пробелы в список (через 1)
        res = [' '] * (2*len(list) - 1)
        res[::2] = list

        double = len([i for i in list if len(i) > 1])
        while len(res) + double < 26:
            rand_index = random.randint(0, len(list) - 1) # В рандомное место вставим пробел
            res.insert(rand_index, ' ')
        return ''.join(res)

    def create_card(self):
        list_str = [0] * 5
        list_str[0], list_str[4] = self._get_bold()
        for i in range(3):
            list_str[1 + i] = self._get_string(self._get_numbers())
        return '\n'.join(list_str)

class Game:

    def __init__(self):
        self._points = 0
        self._numbers = []
        self._computer = Card('PC')
        self._player = Card('Player')

    def _generate_number(self):
        t = 32
        while t in self._numbers:
            t = random.randint(1, 90)
        self._numbers.append(t)
        return t

    def _delete_number(self, number, card):
        card = card.replace(str(number), '-')
        self._points += 1
        return card


    def play(self):
        player_card = self._player.create_card()
        pc_card = self._computer.create_card()
        while self._points < 15:
            number = self._generate_number()
            print(f'Новый бочонок: {number} '
                  f'(осталось {90 - len(self._numbers)})')
            print(player_card)
            print(pc_card)
            is_number_player = (player_card.find(str(number)) > 0)
            is_number_pc = (pc_card.find(str(number)) > 0)
            if input('Зачеркнуть цифру? (y/n)') == 'y':
                if  is_number_player:
                    print('Отлично! Следующий ход:')
                    player_card = self._delete_number(number, player_card)
                    if  is_number_pc:
                        pc_card = self._delete_number(number, pc_card)
                else:
                    print('Такого номера у вас нет! Игра окончена.')
                    break
            else:
                if is_number_player:
                    print('Такой номер у вас был! Игра окончена.')
                    break
                else:
                    print('Отлично! Следующий ход:')
                    if is_number_pc:
                        pc_card = self._delete_number(number, pc_card)
        print('Вы победили!')

game = Game()
game.play()