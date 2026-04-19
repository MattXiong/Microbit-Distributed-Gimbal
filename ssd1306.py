"""
Custom SSD1306 OLED Driver for Micro:bit
---------------------------------------------------------
A lightweight, pure Python driver that bypasses framebuf constraints.
Implements native bitwise pixel mapping and Bresenham's algorithms.
"""

class SSD1306_I2C:
    def __init__(self, width, height, i2c_obj, addr=0x3C):
        self.width = width
        self.height = height
        self.i2c = i2c_obj
        self.addr = addr
        self.pages = self.height // 8
        
        # 1 control byte + 1024 bytes VRAM (for 128x64)
        self.buffer = bytearray(self.pages * self.width + 1)
        self.buffer[0] = 0x40 
        self.init_display()

    def write_cmd(self, cmd):
        self.i2c.write(self.addr, bytearray([0x00, cmd]))

    def init_display(self):
        init_cmds = [
            0xAE, 0x20, 0x00, 0x21, 0, self.width - 1,
            0x22, 0, self.pages - 1, 0x81, 0xCF, 0xA1,
            0xA8, self.height - 1, 0xC8, 0xD3, 0x00,
            0xD5, 0x80, 0xD9, 0xF1, 0xDA, 0x12, 0xDB, 0x40,
            0x8D, 0x14, 0xA6, 0xA4, 0xAF
        ]
        for cmd in init_cmds:
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def show(self):
        self.write_cmd(0x21)
        self.write_cmd(0)
        self.write_cmd(self.width - 1)
        
        self.write_cmd(0x22)
        self.write_cmd(0)
        self.write_cmd(self.pages - 1)
        
        self.i2c.write(self.addr, self.buffer)

    def fill(self, color):
        val = 0xFF if color else 0x00
        for i in range(1, len(self.buffer)):
            self.buffer[i] = val

    def pixel(self, x, y, color):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return
        idx = 1 + int(x) + (int(y) // 8) * self.width
        if color:
            self.buffer[idx] |= (1 << (int(y) % 8))
        else:
            self.buffer[idx] &= ~(1 << (int(y) % 8))

    def fill_rect(self, x, y, w, h, color):
        for i in range(max(0, int(x)), min(self.width, int(x + w))):
            for j in range(max(0, int(y)), min(self.height, int(y + h))):
                self.pixel(i, j, color)

    def rect(self, x, y, w, h, color):
        # Utilizes 4 solid lines for fast empty rectangle rendering
        self.fill_rect(x, y, w, 1, color)            # Top
        self.fill_rect(x, y + h - 1, w, 1, color)    # Bottom
        self.fill_rect(x, y, 1, h, color)            # Left
        self.fill_rect(x + w - 1, y, 1, h, color)    # Right

    def line(self, x0, y0, x1, y1, color):
        # Bresenham's line algorithm
        x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        while True:
            self.pixel(x0, y0, color)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy
