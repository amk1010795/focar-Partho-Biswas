import time
from focar import move, set_led

def run_focar_routine():
    print("--- Starting FoCar Routine ---")
    # Visual indicator that the routine is starting
    set_led(True)
    time.sleep(1)
    
    # 1. Move forward approximately 1 meter
    print("\nStep 1: Moving forward 1 meter...")
    move(speed_left=60, speed_right=60, duration=2.5) # Calibrate time to equal ~1m
    time.sleep(0.5)

    # 2. Perform a Three-Point Turn
    print("\nStep 2: Executing 3-point turn...")
    # Turn 1: Forward and hard right
    print("-> Turn 1: Forward Right")
    move(speed_left=60, speed_right=20, duration=1.5)
    time.sleep(0.5)
    
    # Turn 2: Reverse and hard left
    print("-> Turn 2: Reverse Left")
    move(speed_left=-20, speed_right=-60, duration=1.8)
    time.sleep(0.5)
    
    # Turn 3: Forward left to face back towards the origin
    print("-> Turn 3: Forward Left (Straightening out)")
    move(speed_left=60, speed_right=30, duration=1.2)
    time.sleep(0.5)

    # 3. Return to the starting point
    print("\nStep 3: Returning to starting point...")
    move(speed_left=60, speed_right=60, duration=2.5)
    
    # Turn off LED to indicate routine completion
    set_led(False)
    print("\n--- Routine Finished Successfully ---")

if __name__ == "__main__":
    run_focar_routine()