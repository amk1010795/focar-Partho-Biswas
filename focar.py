from machine import Pin, PWM
from time import sleep

# Motor A Control (Left Motor)
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Motor B Control (Right Motor)
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)     

# Fix lowercase "pin" typo from initial reference to properly instantiate Pico LED
led = Pin("LED", Pin.OUT)

# Configure PWM frequency to 1000 Hz
e1.freq(1000)
e2.freq(1000)

def set_led(status):
    """Controls the onboard status LED (True = ON, False = OFF)."""
    led.value(1 if status else 0)

def stop():
    """Stops both motors immediately by clearing duty cycle values."""
    e1.duty_u16(0)
    e2.duty_u16(0)
    m1.value(0)
    m2.value(0)

def forward(speed=32767, duration=1.0):
    """Drives both motors forward for a designated duration."""
    m1.value(1)
    m2.value(1)
    e1.duty_u16(speed)
    e2.duty_u16(speed)
    sleep(duration)
    stop()

def backward(speed=32767, duration=1.0):
    """Reverses both motors backward for a designated duration."""
    m1.value(0)
    m2.value(0)
    e1.duty_u16(speed)
    e2.duty_u16(speed)
    sleep(duration)
    stop()

def spin_right(speed=32767, duration=0.5):
    """Pivots the robot clockwise in place."""
    m1.value(1)
    m2.value(0)
    e1.duty_u16(speed)
    e2.duty_u16(speed)
    sleep(duration)
    stop()

def spin_left(speed=32767, duration=0.5):
    """Pivots the robot counter-clockwise in place."""
    m1.value(0)
    m2.value(1)
    e1.duty_u16(speed)
    e2.duty_u16(speed)
    sleep(duration)
    stop()