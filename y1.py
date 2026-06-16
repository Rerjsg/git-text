import cv2
import numpy as np

offset_x, offset_y = 400, 400

rects = [
    {'dx': 0, 'dy': 0, 'w': 300, 'h': 80},
    {'dx': 0, 'dy': 100, 'w': 70, 'h': 120},
    {'dx': 0, 'dy': -70, 'w': 120, 'h': 60},
    {'dx': 0, 'dy': 180, 'w': 150, 'h': 60},
]

while True:
    img = np.zeros((800, 800, 3), dtype=np.uint8)

    for r in rects:
        cx = offset_x + r["dx"]
        cy = offset_y + r["dy"]
        half_w = r["w"] // 2
        half_h = r["h"] // 2
        x1 = int(cx - half_w)
        y1 = int(cy - half_h)
        x2 = int(cx + half_w)
        y2 = int(cy + half_h)

        cv2.rectangle(img, (x1, y1), (x2, y2), (230, 216, 173), -1)
        cv2.rectangle(img, (x1, y1), (x2, y2), (193, 182, 255), 2)

    cv2.imshow("Plane", img)

    key = cv2.waitKey(20) & 0xFF
    if key == ord('w'):
        offset_y -= 10
    elif key == ord('s'):
        offset_y += 10
    elif key == ord('a'):
        offset_x -= 10
    elif key == ord('d'):
        offset_x += 10
    elif key == 27:
        break

cv2.destroyAllWindows()
