# main.py
from time import sleep
import focar

# Constant power reference matching 50% duty cycle
SPEED_50 = 32767

# Initial 5-second mandatory safety pause before execution begins
sleep(5)

# Turn indicator light on to signal program launch
focar.set_led(True)

try:
    # 1. Move forward for approximately 1 meter
    # (Adjust duration based on your battery level if it drives too far or short)
    focar.forward(speed=SPEED_50, duration=2.0)
    sleep(0.5)

    # 2. Execute a Three-Point Turn sequence
    # Step A: Swing forward-right
    focar.spin_right(speed=SPEED_50, duration=0.8)
    sleep(0.3)
    
    # Step B: Back up into the left quadrant
    focar.backward(speed=SPEED_50, duration=1.0)
    sleep(0.3)
    
    # Step C: Align straight back into the main travel path
    focar.spin_right(speed=SPEED_50, duration=0.4)
    sleep(0.5)

    # 3. Return to the starting point
    focar.forward(speed=SPEED_50, duration=2.0)

finally:
    # Safe shutdown execution routine
    focar.stop()
    focar.set_led(False)
    print("Assignment sequence completed successfully.")