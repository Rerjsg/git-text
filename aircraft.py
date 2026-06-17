import cv2


class Aircraft:
    h1, w1 = 80, 200
    h2, w2 = 150, 60
    h3, w3 = 60, 100
    # airplanes = []

    def __init__(self, centrex, centrey):
        self.cx = centrex
        self.cy = centrey
        self.r3_cx = centrex
        self.r3_cy = centrey + self.h2//2+self.h3//2

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

    # def mouse_event(self, event):
    #     if event == cv2.EVENT_LBUTTONDOWN:
    #         airplanes.append((self.cx, self.cy))
