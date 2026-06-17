import cv2
import numpy as np
import aircraft


airplanes = []
center_x, center_y = 400, 400
h1, w1 = 80, 200
h2, w2 = 150, 60
h3, w3 = 60, 100
cx = center_x
cy = center_y
r3_cx = cx
r3_cy = cy + h2//2+h3//2
a1 = aircraft.Aircraft(cx, cy)

# selected_plane = None


def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        airplanes.append(aircraft.Aircraft(x, y))


cv2.namedWindow("Plane")
cv2.setMouseCallback("Plane", mouse_event)

while True:
    img = np.zeros((800, 800, 3), dtype=np.uint8)
    for plane in airplanes:
        plane.draw(img)

    cv2.imshow("Plane", img)

    key = cv2.waitKey(20) & 0xFF

    if len(airplanes) > 0:
        airplanes[-1].spin(key)

    if key == 27:
        break


cv2.destroyAllWindows()
