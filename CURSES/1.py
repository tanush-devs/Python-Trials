import curses


def main(stdscr):
  curses.curs_set(0)
  height, width = stdscr.getmaxyx()

  # 1. Create a large pad (100 rows tall, 50 columns wide)
  pad = curses.newpad(100, 50)

  # 2. Fill the pad with content
  for i in range(100):
    pad.addstr(i, 0, f"Line {i}: This is scrollable content!")

  current_line = 0

  while True:
    stdscr.clear()
    stdscr.addstr(
        0, 0, "Use UP/DOWN arrows to scroll (q to quit)", curses.A_BOLD
    )
    stdscr.refresh()

    # 3. Refresh pad: show lines starting from 'current_line'
    # Display area on screen: from (y=2, x=2) to (height-2, width-2)
    pad.refresh(current_line, 0, 2, 2, height - 2, width - 2)

    key = stdscr.getch()

    if key == ord("q"):
      break
    elif key == curses.KEY_DOWN and current_line < 100 - (height - 3):
      current_line += 1
    elif key == curses.KEY_UP and current_line > 0:
      current_line -= 1


curses.wrapper(main)