class Snake:

    def __init__(self):

        self.size = 20

        self.body = [
            [200, 200],
            [180, 200],
            [160, 200]
        ]

        self.dx = self.size
        self.dy = 0

    def move(self):

        head_x = self.body[0][0] + self.dx
        head_y = self.body[0][1] + self.dy

        self.body.insert(0, [head_x, head_y])

        self.body.pop()

    def grow(self):

        tail = self.body[-1]
        self.body.append(tail.copy())

    def eat_food(self, food):

        head = self.body[0]

        return head[0] == food.x and head[1] == food.y

    def hit_self(self):

        head = self.body[0]

        return head in self.body[1:]
