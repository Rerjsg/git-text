import cv2


class Bullet:
    r = 10

    def __init__(self, bulletx, bullety, direction):
        self.bx = bulletx
        self.by = bullety
        self.direction = direction

    def draw(self, img):
        cv2.circle(img, (self.bx, self.by), self.r, (0, 0, 255), -1)

    def move(self):
        if self.direction == 'w':
            self.by -= 10
        elif self.direction == 's':
            self.by += 10
        elif self.direction == 'a':
            self.bx -= 10
        elif self.direction == 'd':
            self.bx += 10
