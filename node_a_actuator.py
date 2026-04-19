"""
Node A: Actuator Controller
---------------------------------------------------------
Drives the 2-DOF gimbal using hardware-level silent PWM 
and linear interpolation (Lerp) for ultra-smooth motion.
"""

from microbit import *
import radio

# Initialize radio communication
radio.on()
radio.config(group=22)

curr_x, curr_y = 90.0, 90.0
target_x, target_y = 90.0, 90.0 

# State variables for hardware debouncing
last_duty_x, last_duty_y = -1, -1

def set_servo(pin, angle, is_x_axis):
    global last_duty_x, last_duty_y
    
    # Constrain physical limits to prevent servo damage
    angle = max(10, min(170, angle))
    duty = int((angle / 180 * 102) + 26)
    
    # PWM Silent Mode: Only transmit signal upon actual value change
    # This eliminates the annoying high-frequency servo humming
    if is_x_axis:
        if abs(duty - last_duty_x) > 0:
            pin.write_analog(duty)
            last_duty_x = duty
    else:
        if abs(duty - last_duty_y) > 0:
            pin.write_analog(duty)
            last_duty_y = duty
            
    pin.set_analog_period(20)

display.show('A')

while True:
    msg = radio.receive()
    if msg:
        try:
            parts = msg.split(',')
            target_x = float(parts[0])
            target_y = float(parts[1])
            display.set_pixel(0, 0, 9)
        except Exception:
            pass
    else:
        display.set_pixel(0, 0, 0)
        
    # Linear Interpolation (Lerp) for organic movement
    # 0.4 represents the perfect balance between responsiveness and smoothness
    curr_x += (target_x - curr_x) * 0.4
    curr_y += (target_y - curr_y) * 0.4
    
    set_servo(pin0, curr_x, True)
    set_servo(pin1, curr_y, False)
    
    sleep(20)
