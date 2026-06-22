import random


class Food:

    def __init__(self, width: int, height: int, size: int) -> None:
        self.width = width
        self.height = height
        self.size = size

        self.x = 0
        self.y = 0

        self.random_pos()

        self.value = 1

    def random_pos(self) -> None:
        self.x = random.randrange(0, self.width // self.size) * self.size
        self.y = random.randrange(0, self.height // self.size) * self.size

        self.value = random.randint(1, 3)
