from threading import Thread
from os import system
from time import sleep


format_one = 0
format_two = 0
format_tre = 0

loop_types = 1


def receive_color():
    global format_one, format_two, format_tre, loop_types

    for types1, types2, types3, number in zip([1, 0], [0, 1], ['+', '-'], [255, 0]):
        if (loop_types == types1):
            if (format_one != number):
                exec(f'format_one {types3}= 15', globals())

            if (format_one == number):
                if (format_two != number):
                    exec(f'format_two {types3}= 15', globals())
                    
            if (format_two == number):
                if (format_tre != number):
                    exec(f'format_tre {types3}= 15', globals())

            if (format_tre == number):
                loop_types = types2
    
    return f"\033[38;2;{format_one};{format_two};{format_tre}m"


def colored_string():
    print(receive_color() + 'color testing')

if (__name__ == '__main__'):
    system('')

    for _ in range(10000000):
        Thread(target=colored_string).start()
        sleep(0.01)
