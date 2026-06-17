import cv2
import numpy as np

center_x, center_y = 400, 400
h1, w1 = 80, 200
h2, w2 = 150, 60
h3, w3 = 60, 100
cx = center_x
cy = center_y
r3_cx = cx
r3_cy = cy + h2//2+h3//2

while True:
    img = np.zeros((800, 800, 3), dtype=np.uint8)

    r1_1 = (cx-w1//2, cy - h1//2)
    r1_2 = (cx+w1//2, cy + h1//2)
    r2_1 = (cx-w2//2, cy-h2//2)
    r2_2 = (cx+w2//2, cy+h2//2)
    r3_1 = (r3_cx-w3//2, r3_cy-h3//2)
    r3_2 = (r3_cx+w3//2, r3_cy+h3//2)
    # a3 = (cx, cy+3*h3//2)
    # d = h3*3//2
    # d1 = (-d, cy)
    # a4 = (-d-w3//2, cy-h3//2)
    # a5 = (-d+w3//2, cy+h3//2)

    cv2.rectangle(img, r1_1, r1_2, (230, 216, 173), -1)
    cv2.rectangle(img, r2_1, r2_2, (230, 216, 173), -1)
    cv2.rectangle(img, r3_1, r3_2, (230, 216, 173), -1)
    cv2.rectangle(img, r1_1, r1_2, (193, 182, 255), 2)
    cv2.rectangle(img, r2_1, r2_2, (193, 182, 255), 2)
    cv2.rectangle(img, r3_1, r3_2, (193, 182, 255), 2)
    cv2.imshow("Plane", img)

    key = cv2.waitKey(20) & 0xFF

    if key == ord('w'):

        r3_cx = cx
        r3_cy = cy + h2//2+h3//2
    elif key == ord('s'):
        r3_cx = cx
        r3_cy = cy - h2//2-h3//2
    elif key == ord('a'):
        h1, w1 = w1, h1
        h2, w2 = w2, h2
        h3, w3 = w3, h3
        r3_cx = cx + h2//2+h3//2
        r3_cy = cy

    elif key == ord('d'):

        r3_cx = cx - h2//2-h3//2
        r3_cy = cy
    elif key == 27:
        break

cv2.destroyAllWindows()
