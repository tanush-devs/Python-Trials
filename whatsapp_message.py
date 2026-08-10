import time

import pyautogui

# --- Configuration ---
START_NUMBER = 362752740  # Change this to your starting number
DELAY_BETWEEN_NUMBERS = 0.5  # Pause in seconds after each number
COUNTDOWN_BEFORE_SWITCH = 2  # Seconds to prepare before starting

def run_whatsapp_countdown(start_num):
    print(f"Starting in {COUNTDOWN_BEFORE_SWITCH} seconds...")
    print("MAKE SURE WHATSAPP IS THE VERY NEXT TAB WHEN YOU PRESS ALT+TAB!")
    
    # Give you a moment to see the prompt in VS Code terminal
    time.sleep(COUNTDOWN_BEFORE_SWITCH)

    # Switch tab to WhatsApp (Alt + Tab)
    pyautogui.hotkey('alt', 'tab')
    
    # Small pause to let the window switch finish
    time.sleep(1)

    # Loop from start_num down to 0
    for _ in range(start_num, -1, -1):
        for char in "JALDI BOL":
            # Type the number
            pyautogui.typewrite(char)
            # Press Enter
            pyautogui.press('enter')
            # Wait before the next number
            time.sleep(DELAY_BETWEEN_NUMBERS)

if __name__ == "__main__":
    # FAIL-SAFE: Move your mouse to any corner of the screen to forcibly stop the script if needed.
    pyautogui.FAILSAFE = True
    
    run_whatsapp_countdown(START_NUMBER)