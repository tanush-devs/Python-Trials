import random
import time

import menus
import rooms
import utils


def game_loop():
    room = list(range(2,6))
    while len(room) > 0:
        utils.clear_terminal()
        next_room = random.choice(room)
        if next_room == 2:
            utils.print_Info("You enter the: 💰 Treasure Room")
            time.sleep(2)
            rooms.room_trasure()

        elif next_room == 3:
            utils.print_Info("You enter the: 🧪 Potion Room")
            time.sleep(2)
            rooms.room_potion()

        elif next_room == 4:
            utils.print_Info("You enter the: 🕳️ Trap Room")
            time.sleep(2)
            rooms.room_trap()

        elif next_room == 5:
            utils.print_Info("You enter the: 🌿 Empty Room")
            time.sleep(2)
            rooms.room_empty()

        input("> ")
        room.remove(next_room)

while True:
    menus.show_main()
    choice = utils.get_func(1,2)
    if choice == 1:
        game_loop()
    elif choice == 2:
        break