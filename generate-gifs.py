from PIL import Image, ImageOps
import math, random

for q in range(10):
    l = q / 10.0
    def near_websafe(x):
        def sh(v):
            noise = random.random() * l
            v = v * (1 + noise)
            return 0x33 * math.floor(v / 0x33)
        return [(sh(r), sh(g), sh(b)) for r, g, b in x]

    i = Image.open('input.jpg')
    i2 = ImageOps.fit(i, (150, 150))
    data = near_websafe(i2.getdata())
    i2.putdata(data)
    i2.save('output%d.gif' % q)
