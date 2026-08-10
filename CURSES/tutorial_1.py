import curses  # noqa: F401
import time
from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0,"Hello gayz")
    stdscr.refresh()
    for index,char in enumerate("Bye gayz    "):
        stdscr.addstr(0,index,char)
        stdscr.refresh()
        time.sleep(0.02)

wrapper(main)