import curses
import time


def get_int(a):
    if int(a) == 0:
        a+=1
    return int(a)

def update_cords(stdscr, x, y, velocity):
  height, width = stdscr.getmaxyx()
  dy, dx = velocity

  if x + dx >= width - 1 or x + dx <= 0:
    dx = -dx
  if y + dy >= height - 1 or y + dy <= 0:
    dy = -dy

  new_x = x + dx
  new_y = y + dy

  return new_x, new_y, (dy, dx)

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)  # Don't pause on getch()
    
    x,y = 1,1
    velocity = (1,2)
    symbol = "@"
    while True:
        # Exit condition
        key = stdscr.getch()
        if key == ord("q"):
            break

        stdscr.clear()
        stdscr.addstr(y, x, symbol)

        x, y, velocity = update_cords(stdscr, x, y, velocity)

        stdscr.refresh()
        time.sleep(0.05)


curses.wrapper(main)
