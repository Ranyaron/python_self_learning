#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_down()
    x = 1
    while x <= 4:
        move_right()
        fill_cell()

        move_right()
        move_down()
        fill_cell()

        move_down()
        move_left()
        fill_cell()

        move_up()
        fill_cell()
        move_left()
        fill_cell()

        move_up()
        x += 1
        move_right(4)

    while x <= 5:
        #for i in range(x):
        move_right()
        fill_cell()

        move_right()
        move_down()
        fill_cell()

        move_down()
        move_left()
        fill_cell()

        move_up()
        fill_cell()
        move_left()
        fill_cell()

        move_up()
        x += 1

if __name__ == '__main__':
    run_tasks()
