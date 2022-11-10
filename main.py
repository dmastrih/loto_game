import random


class Player:
    pass


class Card:
    pass


class Barrel:
    pass


class Pouchs:
    def __init__(self):
        self.count = 90
        self._list_pouchs = []

    def get_pouch(self):
        current_pouch = random.randrange(1, 4)

        if self._list_pouchs:
            while current_pouch in self._list_pouchs:
                current_pouch = random.randrange(1, 4)

        self._list_pouchs.append(current_pouch)
        return current_pouch

    def quantity_info(self):
        self.count -= 1
        return self.count


if __name__ == '__main__':

