import curses


def main(stdscr):
    # Hide cursor and enable key detection
    curses.curs_set(0)
    stdscr.keypad(True)

    # 1. Get terminal dimensions
    screen_h, screen_w = stdscr.getmaxyx()

    # 2. Create a large pad (200 rows x 200 cols)
    pad_h, pad_w = 200, 200
    pad = curses.newpad(pad_h, pad_w)

    # Fill pad with pattern and a center marker
    for y in range(pad_h):
        for x in range(pad_w):
            if y == pad_h // 2 and x == pad_w // 2:
                pad.addch(y, x, 'X', curses.A_BOLD)  # True pad center
            elif y % 10 == 0 or x % 10 == 0:
                pad.addch(y, x, '+')
            else:
                pad.addch(y, x, '.')

    # Add text to the absolute center of the pad
    center_y, center_x = pad_h // 2, pad_w // 2
    pad.addstr(center_y - 1, center_x - 10, "--- PAD CENTER ---", curses.A_REVERSE)

    # 3. Calculate initial top-left corner on the pad to align pad center with screen center
    pad_y = center_y - (screen_h // 2)
    pad_x = center_x - (screen_w // 2)

    while True:
        # Clamp pad coordinates so we don't view outside pad boundaries
        pad_y = max(0, min(pad_y, pad_h - screen_h))
        pad_x = max(0, min(pad_x, pad_w - screen_w))

        # 4. Render pad onto the entire screen area
        pad.refresh(
            pad_y, pad_x,               # Top-left of pad area to show
            0, 0,                       # Top-left of terminal screen
            screen_h - 1, screen_w - 1  # Bottom-right of terminal screen
        )

        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == curses.KEY_UP:
            pad_y -= 1
        elif key == curses.KEY_DOWN:
            pad_y += 1
        elif key == curses.KEY_LEFT:
            pad_x -= 1
        elif key == curses.KEY_RIGHT:
            pad_x += 1

curses.wrapper(main)