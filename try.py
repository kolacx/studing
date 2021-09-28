import sys
import select
import tty
import termios

def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

old_settings = termios.tcgetattr(sys.stdin)

try:
    tty.setcbreak(sys.stdin.fileno())

    while True:

        if isData():
            c = sys.stdin.read(1)
            if c == '\x1b':         # x1b is ESC
                break
            print(c)

finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
