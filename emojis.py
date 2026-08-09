def check_target(current_value, target=10):
    # ANSI Color Codes
    GREEN = "\033[92m"
    RED = "\033[91m"
    GREY = "\033[90m"
    RESET = "\033[0m"

    if current_value > target:
        print(f"{GREEN}↑{RESET} More than {target} ({current_value})")
    elif current_value < target:
        print(f"{RED}↓{RESET} Less than {target} ({current_value})")
    else:
        print(f"{GREY}✓{RESET} Met target exactly ({current_value})")

# Test cases
check_target(12)  # Green up arrow
check_target(10)  # Grey tick
check_target(7)   # Red down arrow
