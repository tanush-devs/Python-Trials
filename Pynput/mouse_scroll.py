from pynput import mouse


def on_scroll(x, y, dx, dy):
    # x, y: current mouse cursor coordinates
    # dx: horizontal scroll direction (-1 for left, 1 for right)
    # dy: vertical scroll direction (-1 for down, 1 for up)
    if dy > 0:
        print(f"Scrolled UP at ({x}, {y})")
    elif dy < 0:
        print(f"Scrolled DOWN at ({x}, {y})")

# Start listening in a non-blocking background thread
listener = mouse.Listener(on_scroll=on_scroll)
listener.start()

# Keep the main thread alive so the program doesn't exit immediately
input("Press Enter to stop listening...\n")
listener.stop()