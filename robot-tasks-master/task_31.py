#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_8_30():
    x = 0
    while True:
        if not wall_is_beneath():
            while not wall_is_beneath():
                move_down()
        while not wall_is_on_the_right() and wall_is_beneath():
            move_right()
            if not wall_is_beneath():
                while not wall_is_beneath():
                    move_down()
            # if wall_is_beneath() and wall_is_on_the_right():
            #     x -= 1
        while not wall_is_on_the_left() and wall_is_beneath():
            move_left()
            if not wall_is_beneath():
                while not wall_is_beneath():
                    move_down()
            if wall_is_beneath() and wall_is_on_the_left():
                x += 1
        if x > 6:
            break

        # while wall_is_beneath() and not wall_is_on_the_left():
        #     move_left()
        #     break


if __name__ == '__main__':
    run_tasks()
