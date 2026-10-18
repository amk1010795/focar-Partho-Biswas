import time

def set_led(status: bool):
    """Turns the FoCar built-in LED ON (True) or OFF (False)."""
    if status:
        print("[FoCar] LED is ON")
        # Hardware specific command here (e.g., GPIO.output(LED_PIN, True))
    else:
        print("[FoCar] LED is OFF")
        # Hardware specific command here (e.g., GPIO.output(LED_PIN, False))

def move(direction: str, duration: float, speed: int = 50):
    """
    Controls FoCar motor movements.
    Directions: 'forward', 'backward', 'left', 'right', 'stop'
    """
    print(f"[FoCar] Moving {direction.upper()} at speed {speed}% for {duration} seconds.")
    # Hardware motor controller commands map here
    time.sleep(duration)
    
def stop():
    """Stops all motor movements."""
    print("[FoCar] Stop motors.")