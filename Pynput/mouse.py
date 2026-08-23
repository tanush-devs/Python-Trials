from pynput.mouse import Controller

mouse = Controller()

while True:
    print(f"Current mouse position ({mouse.position})")