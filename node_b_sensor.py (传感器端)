"""
Node B: Sensor & Motion Brain
---------------------------------------------------------
Calculates 3D spatial vectors, applies RC-grade Expo mixing, 
and executes first-order Low-Pass Filters (LPF).
"""

from microbit import *
import radio
import math

radio.on()
radio.config(group=22, power=7)

offset_roll = 0.0
offset_pitch = 0.0

flt_roll = 0.0
flt_pitch = 0.0

def get_true_angles():
    """Calculate 3D gravity vectors using math.atan2 to prevent gimbal lock"""
    x, y, z = accelerometer.get_values()
    if z == 0: 
        z = 0.001 
    roll = math.atan2(x, -z) * 180 / math.pi
    pitch = math.atan2(y, -z) * 180 / math.pi
    return roll, pitch

def calibrate():
    """Establish zero-point baseline via 20-frame averaging"""
    global offset_roll, offset_pitch
    display.show(Image.CLOCK1)
    r_sum, p_sum = 0.0, 0.0
    for _ in range(20):
        r, p = get_true_angles()
        r_sum += r
        p_sum += p
        sleep(10)
    offset_roll = r_sum / 20
    offset_pitch = p_sum / 20
    display.show(Image.YES)
    sleep(300)
    display.clear()

def apply_expo(tilt, expo=0.75, sensitivity=1.5):
    """
    RC-grade Expo curve algorithm.
    Compresses micro-jitters near the center while maintaining 
    full throw ranges at the extremities.
    """
    tilt = max(-90.0, min(90.0, tilt)) 
    norm = tilt / 90.0 
    curve = norm * ((1.0 - expo) + expo * (norm * norm)) 
    return curve * 90.0 * sensitivity

# Initial boot calibration
calibrate()

while True:
    if button_b.was_pressed():
        calibrate()
        
    raw_r, raw_p = get_true_angles()
    target_r = raw_r - offset_roll
    target_p = raw_p - offset_pitch
    
    # Stage 1: Expo curve processing
    expo_r = apply_expo(target_r)
    expo_p = apply_expo(target_p)
    
    # Stage 2: First-Order Low-Pass Filter (LPF)
    flt_roll = flt_roll * 0.6 + expo_r * 0.4
    flt_pitch = flt_pitch * 0.6 + expo_p * 0.4
    
    # Stage 3: Servo range mapping
    final_x = max(10, min(170, 90 + flt_roll))
    final_y = max(10, min(170, 90 + flt_pitch))
    
    # Transmit absolute clean data
    radio.send(f"{int(final_x)},{int(final_y)}")
    
    sleep(20)
