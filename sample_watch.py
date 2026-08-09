import time
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
import os

def generate_stopwatch(elapsed_time: float) -> Panel:
    """Generates a large text display for the stopwatch inside a terminal panel."""
    hours, remainder = divmod(int(elapsed_time), 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = int((elapsed_time - int(elapsed_time)) * 100)
    
    # Format the time string clearly
    time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
    
    # Create large, stylish text using rich
    display_text = Text(time_str, style="bold bright_green", justify="center")
    
    return Panel(
        display_text,
        title="⏱️ PYTHON TERMINAL STOPWATCH",
        border_style="cyan",
        padding=(1, 2)
    )

def run_stopwatch():
    os.system("cls")
    print("Press Ctrl+C to stop the stopwatch.\n")
    start_time = time.time()
    
    try:
        with Live(refresh_per_second=10) as live:
            while True:
                elapsed_time = time.time() - start_time
                live.update(generate_stopwatch(elapsed_time))
                time.sleep(0.05)
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")

if __name__ == "__main__":
    run_stopwatch()
