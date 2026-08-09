from colorama import Fore, Style

DARK_BG = "\033[48;5;238m"  # Dark gray background
LIGHT_BG = "\033[48;5;250m" # Light gray background
RESET_BG = "\033[0m"          # Resets color back to default

class Themes:
    DANGER = Fore.RED
    SUCCESS = Fore.GREEN + Style.NORMAL
    WARNING = Fore.YELLOW
    INFO = Fore.CYAN
    CONGO = Fore.GREEN + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL + RESET_BG
    TEXT = Fore.WHITE + Style.NORMAL
    BRIGHT_TEXT = Fore.WHITE + Style.BRIGHT
    DEATH_MESSAGE = Fore.RED + Style.BRIGHT + DARK_BG
    NARRATION = Fore.CYAN + Style.DIM