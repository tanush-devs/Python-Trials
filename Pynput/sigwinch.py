import signal


def handle_sigwinch(signum, frame):
    print("\n[EVENT DETECTED] The terminal was just resized!")

# 1. Register the listener
signal.signal(signal.SIGWINCH, handle_sigwinch)

print("Program running. Try resizing your terminal window...")