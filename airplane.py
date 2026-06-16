import cv2
import numpy as np

offset_x, offset_y = 400, 400
angle = 0.0

rects = [
    {'dx': 0, 'dy': 0, 'w': 300, 'h': 80},
    {'dx': 0, 'dy': 100, 'w': 70, 'h': 120},
    {'dx': 0, 'dy': -70, 'w': 120, 'h': 60},
    {'dx': 0, 'dy': 180, 'w': 150, 'h': 60},
]


while True:
    img = np.zeros((800, 800, 3), dtype=np.uint8)

    for r in rects:
        cos_a = np.cos(angle)
        sin_a = np.sin(angle)
        dx_rot = r["dx"] * cos_a - r["dy"] * sin_a
        dy_rot = r["dx"] * sin_a + r["dy"] * cos_a
        cx = offset_x + dx_rot
        cy = offset_y + dy_rot

        half_w = r["w"] // 2
        half_h = r["h"] // 2
        corners = np.array([
            [-half_w, -half_h],
            [half_w, -half_h],
            [half_w,  half_h],
            [-half_w,  half_h]
        ], dtype=np.float32)

        rotated_corners = np.array([
            [x*cos_a - y*sin_a, x*sin_a + y*cos_a] for x, y in corners
        ], dtype=np.int32)

        pts = rotated_corners + np.array([cx, cy], dtype=np.int32)

        cv2.fillPoly(img, [pts], (230, 216, 173))
        cv2.polylines(img, [pts], True, (193, 182, 255), 2)

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

    elif key == ord('q'):
        angle -= 0.2
    elif key == ord('e'):
        angle += 0.2
    elif key == 27:
        break
cv2.destroyAllWindows()
