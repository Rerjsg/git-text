import cv2
import numpy as np


pts = np.array([
    [333, 233],
    [333, 483],
    [533, 483]
], np.int32)

while True:

    img = np.zeros((800, 800, 3), dtype=np.uint8)
    cv2.polylines(img, [pts], True, (193, 182, 255), 10)
    cv2.fillPoly(img, [pts], (230, 216, 173))

    cv2.imshow("Triangle", img)

    key = cv2.waitKey(20) & 0xFF

    if key == ord('w'):
        pts[:, 1] -= 20

    elif key == ord('s'):
        pts[:, 1] += 10

    elif key == ord('a'):
        pts[:, 0] -= 10

    elif key == ord('d'):
        pts[:, 0] += 10

    elif key == 27:
        break

cv2.destroyAllWindows()
