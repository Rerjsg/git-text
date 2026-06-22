import cv2
import numpy as np
import aircraft
import bullet
import enemy
import random


airplanes = []
bullets = []
enemies = []

for i in range(5):
    e = enemy.Enemy(random.randrange(100, 700), random.randrange(100, 500))
    enemies.append(e)


def mouse_event(event: int, x: int, y: int, flags, param) -> None:
    if event == cv2.EVENT_LBUTTONDOWN:
        airplanes.append(aircraft.Aircraft(x, y))


cv2.namedWindow("Plane")
cv2.setMouseCallback("Plane", mouse_event)
a = enemy.Enemy(200, 300)
while True:
    img = np.zeros((800, 1600, 3), dtype=np.uint8)
    img[:] = 0
    for e in enemies:
        e.draw(img)

    for b in bullets:
        b.move()
        b.draw(img)
    for plane in airplanes:
        if plane.direction == 'w':
            plane.cy -= 6
            plane.r3_cy -= 6
        elif plane.direction == 's':
            plane.cy += 6
            plane.r3_cy += 6
        elif plane.direction == 'a':
            plane.cx -= 6
            plane.r3_cx -= 6
        elif plane.direction == 'd':
            plane.cx += 6
            plane.r3_cx += 6
        plane.draw(img)

    cv2.imshow("Plane", img)

    key = cv2.waitKey(20) & 0xFF

    for b in bullets[:]:
        for e in enemies[:]:
            if e.hit(b):
                bullets.remove(b)
                enemies.remove(e)
                new_enemy = enemy.Enemy(0, 0)
                new_enemy.random_pos()
                enemies.append(new_enemy)
                break
    if len(airplanes) > 0:
        airplanes[-1].spin(key)

    if key == ord(' ') and len(airplanes) > 0:
        plane = airplanes[-1]

        bullets.append(bullet.Bullet(plane.cx, plane.cy, plane.direction))
    if key == 27:
        break


cv2.destroyAllWindows()
