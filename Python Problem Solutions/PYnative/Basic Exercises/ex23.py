import time

def countdown_timer(seconds):
    """
    Creates a countdown timer.

    Args:
        seconds (int): The starting number of seconds for the countdown.
    """
    while seconds > 0:
        print(seconds)
        time.sleep(1)  # Pause for 1 second
        seconds -= 1
    print("Time's up!")

# Example usage:
countdown_timer(5)