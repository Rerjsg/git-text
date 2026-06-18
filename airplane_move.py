import cv2
import numpy as np
import aircraft
import bullet


airplanes = []
bullets = []


def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        airplanes.append(aircraft.Aircraft(x, y))


cv2.namedWindow("Plane")
cv2.setMouseCallback("Plane", mouse_event)

while True:
    img = np.zeros((800, 800, 3), dtype=np.uint8)

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

    if len(airplanes) > 0:
        airplanes[-1].spin(key)

    if key == ord(' ') and len(airplanes) > 0:
        plane = airplanes[-1]

        bullets.append(bullet.Bullet(plane.cx, plane.cy, plane.direction))
    if key == 27:
        break


cv2.destroyAllWindows()
