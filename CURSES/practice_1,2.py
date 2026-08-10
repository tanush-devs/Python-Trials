import curses
from curses import wrapper


def show_headder(stdscr):
    height, width = stdscr.getmaxyx()  # noqa: RUF059
    
    curses.init_pair(1 , curses.COLOR_GREEN , curses.COLOR_BLACK)
    curses.init_pair(2 , curses.COLOR_CYAN , curses.COLOR_BLACK)

    p1 = curses.color_pair(1)
    p2 = curses.color_pair(2)
    title = "--- MY FIRST CURSES APP ---"
    x = (width - len(title)) // 2

    stdscr.clear()
    stdscr.addstr(2,x,title , p2)
    stdscr.addstr(4,2,"Status: Active",p1 | curses.A_BOLD)
    stdscr.addstr(6,2,"Press any key to exit...", curses.A_UNDERLINE)
    stdscr.refresh()
    stdscr.getch()
    
wrapper(show_headder)
