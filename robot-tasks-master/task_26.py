#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_2_4():
    x = 1
    for i in range(2):

        while x <= 9:
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

        while x <= 10:
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
            move_down(4)

        while x <= 11:
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

        while x <= 19:
            move_left(4)
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

        while x <= 20:
            move_left(4)
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
            move_down(4)

        ###

        while x <= 9:
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
            move_down(4)

        x = 1

    while x <= 9:
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

    while x <= 10:
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

    move_left(36)


if __name__ == '__main__':
    run_tasks()
