import cv2


class Aircraft:
    h1, w1 = 80, 200
    h2, w2 = 150, 60
    h3, w3 = 60, 100
    direction = "w"

    def __init__(self, centrex, centrey):
        self.cx = centrex
        self.cy = centrey
        self.r3_cx = centrex
        self.r3_cy = centrey + self.h2//2+self.h3//2
        self.selected = False

    def draw(self, img):
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

    def spin(self, key):

        if key == ord('w'):
            if self.direction in ('s', 'w'):

                self.r3_cx = self.cx
                self.r3_cy = self.cy + self.h2//2+self.h3//2

            elif self.direction in ('a', 'd'):
                self.h1, self.w1 = self.w1, self.h1
                self.h2, self.w2 = self.w2, self.h2
                self.h3, self.w3 = self.w3, self.h3
                self.r3_cx = self.cx
                self.r3_cy = self.cy + self.h2//2+self.h3//2

            self.direction = 'w'
        elif key == ord('s'):
            if self.direction in ('s', 'w'):

                self.r3_cx = self.cx
                self.r3_cy = self.cy + self.h2//2+self.h3//2

            elif self.direction in ('a', 'd'):
                self.h1, self.w1 = self.w1, self.h1
                self.h2, self.w2 = self.w2, self.h2
                self.h3, self.w3 = self.w3, self.h3
                self.r3_cx = self.cx
                self.r3_cy = self.cy + self.h2//2+self.h3//2
            self.r3_cx = self.cx
            self.r3_cy = self.cy - self.h2//2-self.h3//2

            self.direction = 's'
        elif key == ord('a'):
            if self.direction in ('a', 'd'):

                self.r3_cx = self.cx
                self.r3_cy = self.cy + self.h2//2+self.h3//2

            elif self.direction in ('s', 'w'):
                self.h1, self.w1 = self.w1, self.h1
                self.h2, self.w2 = self.w2, self.h2
                self.h3, self.w3 = self.w3, self.h3

            self.r3_cx = self.cx + self.h2//2+self.h3//2
            self.r3_cy = self.cy

            self.direction = 'a'
        elif key == ord('d'):
            if self.direction in ('a', 'd'):

                self.r3_cx = self.cx
                self.r3_cy = self.cy + self.h2//2+self.h3//2

            elif self.direction in ('s', 'w'):
                self.h1, self.w1 = self.w1, self.h1
                self.h2, self.w2 = self.w2, self.h2
                self.h3, self.w3 = self.w3, self.h3
                self.r3_cx = self.cx
                self.r3_cy = self.cy + self.h2//2+self.h3//2
            self.r3_cx = self.cx - self.h2//2-self.h3//2
            self.r3_cy = self.cy
            self.direction = 'd'
