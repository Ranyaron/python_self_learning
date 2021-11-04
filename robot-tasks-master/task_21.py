#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.03)
def task_4_11():
    x = 12
    y = 10
    move_down()
    move_right()
    for i in range(3):
        for i in range(x):
            fill_cell()
            move_down()
            fill_cell()
            move_right()
        x -= 4
        fill_cell()
        move_left(2)
        for i in range(y):
            fill_cell()
            move_left()
            fill_cell()
            move_up()
        y -= 4
        fill_cell()
        move_down(2)
    fill_cell()
    move_down()


if __name__ == '__main__':
    run_tasks()
