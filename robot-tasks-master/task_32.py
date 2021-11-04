#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    # mov(r, v) Поместить значение v в регистр r
    n = 1
    fill_cell()
    while True:
        if not wall_is_on_the_right():
            move_right()
            if not wall_is_beneath():
                break
        while wall_is_above() and wall_is_beneath():
            if cell_is_filled():
                n += 1
            fill_cell()
            if cell_is_filled():
                n += 1
            move_right()
            if not wall_is_beneath():
                break
            # else:
            #     break
        if not wall_is_above() and not wall_is_on_the_right():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    n += 1
                if not cell_is_filled():
                    # n += 1
                    fill_cell()
            while not wall_is_beneath():
                move_down()
    mov('ax', n)


if __name__ == '__main__':
    run_tasks()
