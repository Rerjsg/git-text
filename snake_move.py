import cv2
import numpy as np

from snake import Snake
from food import Food


WIDTH = 800
HEIGHT = 600
SIZE = 20


snake = Snake()
food = Food(WIDTH, HEIGHT, SIZE)


while True:

    img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)

    key = cv2.waitKey(100)

    if key == ord('w'):
        snake.dx = 0
        snake.dy = -SIZE

    elif key == ord('s'):
        snake.dx = 0
        snake.dy = SIZE

    elif key == ord('a'):
        snake.dx = -SIZE
        snake.dy = 0

    elif key == ord('d'):
        snake.dx = SIZE
        snake.dy = 0

    elif key == 27:
        break

    snake.move()

    if snake.eat_food(food):

        snake.grow()

        food.random_pos()

    if snake.hit_self():

        print("Game Over")
        break

    for x, y in snake.body:

        cv2.rectangle(
            img,
            (x, y),
            (x + SIZE, y + SIZE),
            (0, 255, 0),
            -1
        )

    cv2.circle(
        img,
        (food.x + SIZE // 2, food.y + SIZE // 2),
        SIZE // 2,
        (0, 0, 255),
        -1
    )

    cv2.imshow("Snake", img)

cv2.destroyAllWindows()
