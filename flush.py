import random
import time


def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()

def start_game():
    print_slow("🏰 You wake up in a dark, damp dungeon. Cold air chills your spine.")
    print_slow("In front of you are two heavy doors: [1] Left Door or [2] Right Door?")
    
    choice = input("\nWhich door do you open? (1 or 2): ").strip()
    
    if choice == '1':
        print_slow("\n🚪 You push open the Left Door...")
        print_slow("A sleeping dragon is resting on a pile of gold! 🐲")
        action = input("Do you [1] Sneak past or [2] Grab a gold coin? ").strip()
        
        if action == '1':
            print_slow("\nYou tiptoe softly... and find a hidden exit! You ESCAPED! 🎉")
        else:
            print_slow("\n*CLINK!* The dragon wakes up and roasts you! Game Over! 🔥💀")
            
    elif choice == '2':
        print_slow("\n🚪 You push open the Right Door...")
        print_slow("You fall straight into a pit of wild snakes! 🐍")
        luck = random.choice([True, False])
        
        if luck:
            print_slow("Luckily, you find a rope hanging from above and climb out to safety! 🧗‍♂️")
        else:
            print_slow("The snakes bite! You didn't make it. Game Over! ☠️")
            
    else:
        print_slow("\nYou hesitated too long, and a ghost caught you! Game Over! 👻")

if __name__ == "__main__":
    start_game()