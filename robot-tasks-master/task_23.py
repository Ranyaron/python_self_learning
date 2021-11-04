#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.03)
def task_6_6():
    while True:
        if not wall_is_on_the_right():
            move_right()
        while wall_is_above() and wall_is_beneath():
            if not wall_is_on_the_right():
                move_right()
            else:
                break
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                fill_cell()
            while not wall_is_beneath():
                move_down()
        if wall_is_on_the_right():
            while wall_is_beneath():
                move_left()
            break


if __name__ == '__main__':
    run_tasks()
