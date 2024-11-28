# synda/utils.py
import time
import random

def print_letter_by_letter(text, delay_range=(0.01, 0.05)):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(*delay_range))
    print()  # New line at the end

def display_startup_effect():
    print("\n" * 2)
    startup_messages = [
        "Initializing Synda...",
        "Loading AI modules...",
        "Connecting to Twitter API...",
        "Calibrating response algorithms...",
        "Warming up tweet generator..."
    ]
    
    for message in startup_messages:
        print_letter_by_letter(message)
        time.sleep(0.5)
    
    print_letter_by_letter("\nStartup complete!")
    time.sleep(1)
    print("\n" * 2)
