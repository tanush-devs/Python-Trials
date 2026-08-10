import curses  # noqa: F401
from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0,40,"Hello guyz")
    stdscr.refresh()


wrapper(main)