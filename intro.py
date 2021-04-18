import pgzrun
import random

ball = Actor('ball')
ball.pos = 250, 250

WIDTH = 500
HEIGHT = 500
speed_x = random.randint(1,5)
speed_y = random.randint(1,5)
dir_x = 1
dir_y = 1
def draw():
    screen.clear()
    ball.draw()

def update():
    global dir_x
    global dir_y
    ball.left += speed_x*dir_x
    ball.top += speed_y*dir_y
    if ball.left<0 or ball.right > WIDTH:
        dir_x *= -1
    if ball.top<0 or ball.bottom > HEIGHT:
        dir_y *= -1
        

















pgzrun.go()
