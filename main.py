import random


class Card:

    def __init__(self, player):
        self.player = player
        self._width = 9
        self._height = 3
        self._empty = 4
        self._list_pouchs = []
        self._card_list = []

        while len(self._list_pouchs) != 15:
            pouch = random.randrange(1, 91)

            if pouch not in self._list_pouchs:
                self._list_pouchs.append(pouch)

        for i in range(0, self._height):
            sorted_pouch = sorted(self._list_pouchs[5 * i: 5 * (i + 1)])
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


class Barrel:
    pass


class Pouchs:
    def __init__(self):
        self.count = 90
        self._list_pouchs = []

    def get_pouch(self):
        current_pouch = random.randrange(1, 91)

        while current_pouch in self._list_pouchs:
            current_pouch = random.randrange(1, 91)

        self._list_pouchs.append(current_pouch)
        return current_pouch

    def quantity_info(self):
        self.count -= 1
        return self.count


if __name__ == '__main__':
    c = Card("user")
    print(c._card_list)
    print(c)



