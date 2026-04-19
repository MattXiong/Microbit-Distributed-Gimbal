"""
Node C: Bionic Morphological Engine
---------------------------------------------------------
A 6-parameter custom matrix rendering engine featuring 
organic transitions, random saccades, and blink mechanics.
"""

from microbit import *
import radio
import random
from ssd1306 import SSD1306_I2C

# Hardware Init
radio.on()
radio.config(group=22)
i2c.init(freq=400000, sda=pin20, scl=pin19)
oled = SSD1306_I2C(128, 64, i2c)

curr_x, curr_y = 90.0, 90.0
target_x, target_y = 90.0, 90.0 

# Bionic 6-Parameter Morphological States
# Format: [Left Height, Right Height, Top L-Tilt, Top R-Tilt, Bot L-Tilt, Bot R-Tilt]
STATES = {
    "neutral":    [34.0, 34.0,   0.0,   0.0,  0.0,  0.0],
    "angry":      [28.0, 28.0,  12.0, -12.0,  0.0,  0.0],
    "sad":        [28.0, 28.0, -10.0,  10.0,  0.0,  0.0],
    "happy":      [24.0, 24.0,   0.0,   0.0,  8.0, -8.0],
    "surprised":  [48.0, 48.0,   0.0,   0.0,  0.0,  0.0],
    "sleepy":     [12.0, 12.0,  -3.0,   3.0,  0.0,  0.0],
    "suspicious": [16.0, 34.0,  -4.0,   0.0,  0.0,  0.0],
    "confused":   [36.0, 22.0,   8.0,  -4.0,  0.0,  0.0],
    "blink":      [ 4.0,  4.0,   0.0,   0.0,  0.0,  0.0]
}

curr_params = [34.0, 34.0, 0.0, 0.0, 0.0, 0.0]
current_mood = "neutral"
last_mood_change = running_time()
mood_duration = 3000

# Blink Mechanics
last_blink = running_time()
blink_interval = random.randint(800, 2500)
is_blinking = False

# Saccades (Micro eye twitches)
curr_sac_x, curr_sac_y = 0.0, 0.0
target_sac_x, target_sac_y = 0.0, 0.0
last_sac = running_time()

def draw_parametric_eye(cx, cy, w, h, top_tilt, bottom_tilt):
    """High-speed trapezoidal matrix rendering natively on SSD1306"""
    start_x = int(cx - w / 2)
    for col in range(w):
        nx = (col - w / 2) / (w / 2)
        y_top = int(cy - h / 2 + nx * top_tilt)
        y_bottom = int(cy + h / 2 + nx * bottom_tilt)
        
        # Corner anti-aliasing logic
        if col == 0 or col == w - 1:
            y_top += 3; y_bottom -= 3
        elif col == 1 or col == w - 2:
            y_top += 1; y_bottom -= 1
            
        h_col = y_bottom - y_top
        if h_col > 0:
            oled.fill_rect(start_x + col, y_top, 1, h_col, 1)

display.show('O')

while True:
    now = running_time()
    
    msg = radio.receive()
    if msg:
        try:
            parts = msg.split(',')
            target_x = float(parts[0])
            target_y = float(parts[1])
        except Exception:
            pass

    # Visual Sync & Saccades Injection
    curr_x += (target_x - curr_x) * 0.4
    curr_y += (target_y - curr_y) * 0.4
    
    if now - last_sac > random.randint(800, 2000):
        if random.random() > 0.5:
            target_sac_x = random.uniform(-6, 6)
            target_sac_y = random.uniform(-4, 4)
        else:
            target_sac_x, target_sac_y = 0.0, 0.0
        last_sac = now
        
    curr_sac_x += (target_sac_x - curr_sac_x) * 0.5
    curr_sac_y += (target_sac_y - curr_sac_y) * 0.5

    # Autonomic Emotion Engine
    if not is_blinking:
        if now - last_mood_change > mood_duration:
            mood_pool = ["neutral", "neutral", "neutral", "happy", "sad", "angry", "surprised", "sleepy", "suspicious", "confused"]
            current_mood = random.choice(mood_pool)
            mood_duration = random.randint(2000, 5000)
            last_mood_change = now
            
        if now - last_blink > blink_interval:
            is_blinking = True
            last_blink = now
    else:
        if now - last_blink > 120:
            is_blinking = False
            last_blink = now
            blink_interval = random.randint(800, 2500) 
            
    target_params = STATES["blink"] if is_blinking else STATES[current_mood]

    # Morphological Lerp Transition
    for i in range(6):
        curr_params[i] += (target_params[i] - curr_params[i]) * 0.4

    # Frame Composition
    oled.fill(0)
    
    gaze_x = int((curr_x - 90.0) / 80.0 * 20.0 + curr_sac_x)
    gaze_y = int((curr_y - 90.0) / 80.0 * -12.0 + curr_sac_y)
    
    cur_h_l, cur_h_r, cur_tt_l, cur_tt_r, cur_bt_l, cur_bt_r = curr_params
    
    draw_parametric_eye(36 + gaze_x, 32 + gaze_y, 26, cur_h_l, cur_tt_l, cur_bt_l)
    draw_parametric_eye(92 + gaze_x, 32 + gaze_y, 26, cur_h_r, cur_tt_r, cur_bt_r)
    
    oled.show()
    sleep(20)
