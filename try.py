import sys
import select
import tty
import termios


def isData():
    return select.select([sys.stdin], [], [], 1) == ([sys.stdin], [], [])


old_settings = termios.tcgetattr(sys.stdin)

from tqdm import tqdm

speed = tqdm()
rpm = tqdm()

try:
    tty.setcbreak(sys.stdin.fileno())

    i = 0
    while True:
        i += 1
        speed.total = 100
        rpm.total = 100

        speed.iterable = i
        rpm.iterable = i

        speed.update()
        rpm.update()

        if isData():
            c = sys.stdin.read(1)

            if c == 'q':         # x1b is ESC
                break
            # print(c)

finally:
    speed.close()
    rpm.close()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
