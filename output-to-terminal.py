from PIL import Image, ImageOps
import math, random, sys

def near_websafe(x):
    def sh(v):
        noise = random.random() * 0.5
        v = v * (1 + noise)
        return 0x33 * math.floor(v / 0x33)
    return [(sh(r), sh(g), sh(b)) for r, g, b in x]

i = Image.open('input.jpg')
sz = 72
i2 = ImageOps.fit(i, (sz, sz))
data = near_websafe(i2.getdata())
for y in range(sz):
    for x in range(sz):
        rgb = i2.getpixel((x, y))
        sys.stdout.write("\x1b[48;2;%d;%d;%dm  " % rgb)
    sys.stdout.write("\n")
sys.stdout.write("\x1b[0m\n");
