import curses
import curses.textpad
import locale
import time

locale.setlocale(locale.LC_ALL, "")

# Clean ASCII maze grid for internal movement calculations
MAZE = [
    "#############################################",
    "#...#.......#.......#.......#.......#......T#",
    "#.###.#####.#.#####.#.#####.#.#####.#####.#.#",
    "#.#...#...#.#...#...#.....#.#.#...#.#.....#.#",
    "#.#.###.#.#.###.#.#######.#.#.#.#.#.#.#####.#",
    "#.#...#.#.#...#.#...T...#.#...#.#.#.#.#...#.#",
    "#.###.#.#.###.#####.###.#######.#.#.###.#.#.#",
    "#...#.#.#...#.....#...#.#.....#.#.#...#.#.#.#",
    "###.#.#.###.#####.###.#.#.###.#.#.###.#.#.#.#",
    "#...#.#...#.#...#...#.#.#.#.#.#...#...#.#.#.#",
    "#T###.###.#.#.#.###.#.#.#.#....####.###.#.#.#",
    "#.#.....#.#.#.#...#.#.#.#.#.#.....#...#.#.#.#",
    "#.#.#####.#.#.###.#.#.#.#.#.#####.###.#.#.#.#",
    "#.#.#.....#.#...#.#...#.#.#.#.....#...#.#.#.#",
    "#.#.#.#####.###.#.#####.#.#.#.#####.###.#.#.#",
    "#.#.#...#...#...#.....#.#.#.#.#...#...#.#.#.#",
    "#.#.###.#.###.#######.#.#.#.#.#.#.###.#.#.#.#",
    "#.#...#.#...#.#.....#.#...#.#.#.#...#.#...#.#",
    "#.###.#.###.#.#.###.#.#####.#.#.###.#.#####.#",
    "#.....#...#.#.#...#.#.....#.#.#...#.#.....#.#",
    "#.#######.#.#.###.#######.#.#.###.#######.#.#",
    "#.#.....#.#.#...#...T...#.#.#...#.......#.#.#",
    "#.#.###.#.#.#######.###.#.#.###.#######.#.#.#",
    "#...T.....#.........T...#.....#........E#",
    "#############################################",
]

# Universal rendering symbols (Works in 100% of Windows fonts)
RENDER_MAP = {
    "#": "██",  # Solid Wall
    ".": "  ",  # Path
    "P": " @",  # Player
    "T": "▲ ",  # Trap
    "E": "★ ",  # Goal
}

HEIGHT_MAZE = len(MAZE)
LENGTH_MAZE = len(MAZE[0])

plr = {"current_message": "", "steps_taken": 0, "HP": 100}


def next_block(cords):
    x, y = cords
    element = MAZE[y - 1][x - 1]
    if element == "#":
        return 0  # Wall
    elif element == "E":
        return 1  # Exit
    elif element == "T":
        # Clear trap from map upon trigger
        MAZE[y - 1] = MAZE[y - 1][: x - 1] + "." + MAZE[y - 1][x:]
        return 2  # Trap
    return 3


def move_player(cords, next_cords):
    block = next_block(next_cords)
    plr["steps_taken"] += 1

    if block == 0:
        plr["current_message"] = "Cannot walk through a wall!"
        return cords
    if block == 1:
        plr["current_message"] = "CONGRATS! YOU FOUND THE EXIT!"
        plr["steps_taken"] = 0
        return (2, 2)
    if block == 2:
        plr["current_message"] = "OUCH! Stepped on a trap! -20 HP"
        plr["HP"] -= 20
        return next_cords

    plr["current_message"] = ""
    return next_cords


def show_stats(stats_win):
    stats_win.clear()
    text = f"HP: {plr['HP']}\nSteps Taken: {plr['steps_taken']}\nStatus: Exploring..."
    stats_win.addstr(text)
    stats_win.refresh()


def render_maze(cords):
    x, y = cords
    disp_maze = []

    for r_idx, row in enumerate(MAZE):
        rendered_row = ""
        for c_idx, char in enumerate(row):
            if r_idx == (y - 1) and c_idx == (x - 1):
                rendered_row += RENDER_MAP["P"]
            else:
                rendered_row += RENDER_MAP.get(char, "  ")
        disp_maze.append(rendered_row)

    return disp_maze


def main(stdscr):
    curses.curs_set(0)  # Hide blinking text cursor
    stdscr.nodelay(True)

    # Windows creation
    maze = curses.newwin(HEIGHT_MAZE, LENGTH_MAZE * 2 + 1, 1, 1)
    messages = curses.newwin(3, LENGTH_MAZE * 2 + 8, HEIGHT_MAZE + 3, 1)
    stats = curses.newwin(HEIGHT_MAZE, 25, 1, LENGTH_MAZE * 2 + 4)

    # Outer border boxes
    curses.textpad.rectangle(
        stdscr, 0, LENGTH_MAZE * 2 + 3, HEIGHT_MAZE + 1, LENGTH_MAZE * 2 + 28
    )
    curses.textpad.rectangle(
        stdscr, HEIGHT_MAZE + 2, 0, HEIGHT_MAZE + 6, LENGTH_MAZE * 2 + 28
    )
    curses.textpad.rectangle(stdscr, 0, 0, HEIGHT_MAZE + 1, LENGTH_MAZE * 2 + 2)

    cords = (2, 2)  # Player start position

    while True:
        messages.clear()
        maze.clear()
        show_stats(stats)

        if plr["HP"] <= 0:
            stdscr.clear()
            stdscr.addstr(1, 1, "YOU DIED... Game Over!")
            stdscr.refresh()
            stdscr.nodelay(False)
            stdscr.getch()
            return

        key = stdscr.getch()

        if key == curses.KEY_UP:
            cords = move_player(cords, (cords[0], cords[1] - 1))
        elif key == curses.KEY_DOWN:
            cords = move_player(cords, (cords[0], cords[1] + 1))
        elif key == curses.KEY_LEFT:
            cords = move_player(cords, (cords[0] - 1, cords[1]))
        elif key == curses.KEY_RIGHT:
            cords = move_player(cords, (cords[0] + 1, cords[1]))
        elif key == 27:  # ESC key to exit
            return

        disp_maze = render_maze(cords)
        for z, line in enumerate(disp_maze):
            try:
                maze.addstr(z, 0, line)
            except curses.error:
                pass

        messages.addstr(0, 0, plr["current_message"])
        stdscr.refresh()
        maze.refresh()
        messages.refresh()
        stdscr.move(0, 0)
        time.sleep(0.05)


if __name__ == "__main__":
    curses.wrapper(main)