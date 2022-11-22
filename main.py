import random


class Card:

    def __init__(self, player):
        self.player = player
        self._width = 9
        self._height = 3
        self._empty = 4
        self._list_barrels = []
        self._card_list = []

        while len(self._list_barrels) != 15:
            pouch = random.randrange(1, 91)

            if pouch not in self._list_barrels:
                self._list_barrels.append(pouch)

        for i in range(0, self._height):
            sorted_pouch = sorted(self._list_barrels[5 * i: 5 * (i + 1)])
            for j in range(0, self._empty):
                index = random.randint(0, len(sorted_pouch))
                sorted_pouch.insert(index, 0)
            self._card_list += sorted_pouch

    def __str__(self):
        down_line = "------------------------" + "\n"
        for ind, num in enumerate(self._card_list):
            if num == -1:
                down_line += " -"
            elif num == 0:
                down_line += "  "
            else:
                down_line += ' ' + str(num)

            if (ind + 1) % 9 == 0:
                down_line += "\n"

        return down_line + "------------------------"

    def change_card_list(self, pouch):
        if pouch in self._card_list:
            self._card_list[self._card_list.index(pouch)] = -1

    def __contains__(self, item):
        return item in self._card_list

    def game_over(self):
        return set(self._card_list) == {0, -1}


class Pouch:
    def __init__(self):
        self.count = 90
        self._list_barrels = []

    def get_barrel(self):
        current_barrel = random.randrange(1, 91)

        while current_barrel in self._list_barrels:
            current_barrel = random.randrange(1, 91)

        self._list_barrels.append(current_barrel)
        return current_barrel

    def quantity_info(self):
        self.count -= 1
        return self.count


class Game:

    def __init__(self, player_1="User1", player_2="Computer1"):
        self.player_1 = Card(player_1)
        self.player_2 = Card(player_2)
        self.pouch = Pouch()

    def game_round(self):
        barrel = self.pouch.get_barrel()
        balance = self.pouch.quantity_info()
        print(f"Новый бочонок: {barrel} (осталось {balance})")
        print(f"__Карточка {self.player_1.player}__\n{self.player_1}")
        print(f"__Карточка {self.player_2.player}__\n{self.player_2}")

        for user in [self.player_1, self.player_2]:
            if user.player[:-1] == "Computer":
                if barrel in user:
                    user.change_card_list(barrel)
                    if user.game_over():
                        return f"{user.player} win!"

            if user.player[:-1] == "User":

                user_answer = input(
                    f"{user.player} Зачеркнуть цифру или продолжить? (з/п):").lower().strip()

                if (user_answer == "з" and barrel not in user) or (
                        user_answer == "п" and barrel in user):
                    return f"{user.player} lose"

                if barrel in user:
                    user.change_card_list(barrel)
                    if user.game_over():
                        return f"{user.player} win!"


def start_game():
    parameters = input("1 - Игра по умолчанию (User/Computer)\n" + "2 - (Computer/Computer)\n"
                       + "3 - (User/User)\n" + "Выберите тип играков (1, 2, 3) :")

    if parameters == "1":
        new_game = Game()
    elif parameters == "2":
        new_game = Game("Computer1", "Computer2")
    elif parameters == "3":
        new_game = Game("User1", "User2")
    else:
        print("Указанное значение не корректно!")

    while True:
        one_step = new_game.game_round()
        if one_step == "Computer1 win!":
            print("Computer1 win!")
            break
        elif one_step == "Computer2 win!":
            print("Computer1 win")
            break
        elif one_step == "User1 win!":
            print("User1 win!")
            break
        elif one_step == "User2 win!":
            print("User2 win!")
            break
        elif one_step == "User1 lose":
            print("User1 lose")
            break
        elif one_step == "User2 lose":
            print("User2 lose")
            break


if __name__ == '__main__':
    start_game()
