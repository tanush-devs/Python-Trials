import sys, time

# Global state
player = {"hp": 20, "max_hp": 20, "gold": 15}

def init_split_screen(hud_lines=3, max_terminal_lines=24):
    """Locks lines 1..hud_lines as static overlay; lines (hud_lines+1)..24 scroll."""
    sys.stdout.write(f"\033[{hud_lines + 1};{max_terminal_lines}r")
    sys.stdout.write(f"\033[{hud_lines + 1};1H")  # Move cursor to log start
    sys.stdout.flush()

# --- EVENT 1: UPDATE OVERLAY ONLY (Does NOT touch story text/cursor) ---
def update_hud():
    # Save current cursor position in the game log
    sys.stdout.write("\033[s") 
    
    # Move to top-left (Line 1, Col 1)
    sys.stdout.write("\033[1;1H") 
    
    # Overwrite just the HUD lines
    print("┌" + "─"*48 + "┐")
    print(f"│  ❤️ HP: {player['hp']}/{player['max_hp']:<2}  |  🪙 GOLD: {player['gold']:<4}                   │")
    print("└" + "─"*48 + "┘")
    
    # Instantly jump back to wherever the player was reading/typing!
    sys.stdout.write("\033[u")
    sys.stdout.flush()

# --- EVENT 2: LOG PRINTING ONLY (Does NOT touch top HUD) ---
def log(text):
    """Normal story/combat print function."""
    print(text)

def restore_terminal():
    """Resets margins when quitting."""
    sys.stdout.write("\033[r\033[2J\033[1;1H")
    sys.stdout.flush()
    
try:
    init_split_screen(hud_lines=3)
    update_hud() # Initial load

    # --- MAIN SCREEN CHANGE (Story event) ---
    log(" You enter the: 🐺 Monster Room")
    log("A giant Dire Wolf blocks your path!")
    time.sleep(1.5)

    # --- OVERLAY CHANGE ONLY (Poison ticks down silently) ---
    # HP updates at the top, but NO new text prints in the middle!
    player["hp"] -= 2
    update_hud() 
    time.sleep(1)

    # --- MAIN SCREEN CHANGE (Player turn) ---
    log("\nWhat is your move?")
    log("1. Attack\n2. Block")
    choice = input("> ")

    # --- BOTH CHANGE AT DIFFERENT DELAYS ---
    if choice == "1":
        log("\n⚔️ You slashed the wolf!")
        time.sleep(0.8)
        
        log("💥 The wolf counter-attacked!")
        player["hp"] -= 6
        update_hud() # Overlay reflects -6 HP right on impact!

finally:
    restore_terminal()