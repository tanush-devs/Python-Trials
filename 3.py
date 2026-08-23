import curses


def main(stdscr):
    stdscr.addstr(" \u26A1")
    print(" \u26A1")
    stdscr.refresh()
    stdscr.getch()
    
curses.wrapper(main)