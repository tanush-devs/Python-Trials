from pynput import mouse


def on_move(x,y):
    print(f"New position: ({x},{y})")

# blocking way
with mouse.Listener(on_move=on_move) as listener:
    listener.join()


# Non blocking way
listener = mouse.Listener(on_move=on_move)
listener.start()



# last_x = 0
# last_y = 0

# while True:
#     x,y = mouse.position

#     if x != last_x or y != last_y:
#         last_x = x
#         last_y = y

#         print(f"New position: ({x},{y})")