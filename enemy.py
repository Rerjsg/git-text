import cv2
import random
from bullet import Bullet


class Enemy:
    h1, w1 = 40, 100
    h2, w2 = 75, 30
    h3, w3 = 30, 50

    def __init__(self, centrex: int, centrey: int) -> None:
        self.cx = centrex
        self.cy = centrey
        self.r3_cx = centrex
        self.r3_cy = centrey + self.h2//2+self.h3//2

    def draw(self, img) -> None:
        r1_1 = (self.cx-self.w1//2, self.cy - self.h1//2)
        r1_2 = (self.cx+self.w1//2, self.cy + self.h1//2)
        r2_1 = (self.cx-self.w2//2, self.cy-self.h2//2)
        r2_2 = (self.cx+self.w2//2, self.cy+self.h2//2)
        r3_1 = (self.r3_cx-self.w3//2, self.r3_cy-self.h3//2)
        r3_2 = (self.r3_cx+self.w3//2, self.r3_cy+self.h3//2)

        cv2.rectangle(img, r1_1, r1_2, (230, 216, 173), -1)
        cv2.rectangle(img, r2_1, r2_2, (230, 216, 173), -1)
        cv2.rectangle(img, r3_1, r3_2, (230, 216, 173), -1)
        cv2.rectangle(img, r1_1, r1_2, (193, 182, 255), 2)
        cv2.rectangle(img, r2_1, r2_2, (193, 182, 255), 2)
        cv2.rectangle(img, r3_1, r3_2, (193, 182, 255), 2)

    def random_pos(self) -> None:
        self.cx = random.randrange(50, 1550)
        self.cy = random.randrange(50, 700)
        self.r3_cx = self.cx
        self.r3_cy = self.cy + self.h2//2 + self.h3//2

    def hit(self, bullet: Bullet) -> bool:
        left = self.cx - self.w1//2
        right = self.cx + self.w1//2
        top = self.cy - self.h2//2
        bottom = self.r3_cy + self.h3//2

        return (left <= bullet.bx <= right and top <= bullet.by <= bottom)
