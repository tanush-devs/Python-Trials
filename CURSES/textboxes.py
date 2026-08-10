import curses
from curses.textpad import Textbox, rectangle

'''def reset_window(textbox_window):
    # 1. Clear the window associated with the textbox
    textbox_window.clear()

    # 2. Move the window's cursor back to the top-left corner (0, 0)
    textbox_window.move(0, 0)

    # 3. Refresh the window to apply the visual changes
    textbox_window.refresh()
    

def main(stdscr):
    final_text = []
    while True:
        curses.init_pair(1 , curses.COLOR_GREEN , curses.COLOR_BLACK)
        curses.init_pair(2 , curses.COLOR_CYAN , curses.COLOR_WHITE)
    
        p1 = curses.color_pair(1)
        p2 = curses.color_pair(2)
        
        height , width = stdscr.getmaxyx()  # noqa: RUF059
        output = curses.newwin(10, width-2, 1,1)
        input = curses.newwin(1, width -2, 13,1)
        
        rectangle(stdscr, 0,0 , 11, width-1)
        rectangle(stdscr, 12,0 , 16, width-1)

        output.addstr("\n".join(final_text),p1)
        stdscr.refresh()
        output.refresh()
        
        box = Textbox(input)
        
        reset_window(input)
        box.edit()
        text = box.gather().strip()
        if text.lower() == "exit":
            return
        final_text.append(text)


    
curses.wrapper(main)'''

# GEMINI VERSION


# Fix: Pressing 'Enter' terminates the box instead of needing Ctrl+G
def enter_to_submit(ch):
  if ch in (10, 13):
    return 7  # ASCII 7 is Ctrl+G
  return ch


def main(stdscr):
  curses.curs_set(1)  # Show cursor for typing

  # 1. SETUP ONCE (Outside the loop!)
  curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
  p1 = curses.color_pair(1)

  _height, width = stdscr.getmaxyx()

  # Draw static borders once
  rectangle(stdscr, 0, 0, 11, width - 1)
  rectangle(stdscr, 12, 0, 14, width - 1)
  stdscr.refresh()

  # Create windows once
  output_win = curses.newwin(10, width - 2, 1, 1)
  input_win = curses.newwin(1, width - 2, 13, 1)

  box = Textbox(input_win)
  final_text = []

  # 2. LOOP ONLY FOR DATA & RE-RENDERING
  while True:
    # Update Output
    output_win.clear()
    output_win.addstr("\n".join(final_text[-10:]), p1)  # Show last 10 lines
    output_win.refresh()

    # Get Input
    input_win.clear()
    input_win.move(0, 0)

    # Use validator so 'Enter' key works smoothly!
    box.edit(enter_to_submit)

    text = box.gather().strip()
    if text.lower() == "exit":
      break

    if text:
      final_text.append(text)


curses.wrapper(main)