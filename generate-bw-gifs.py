from PIL import Image, ImageOps
import math, random
import glob

def near_websafe(x):
    def sh(v):
        one_off = random.random()
        noise = one_off * 0.5
        v = v * (1 + noise)
        return 0x33 * math.floor(v / 0x33)
    q = [(sh(r), sh(r), sh(r)) for r, g, b in x]
    q = [(r, r, r) for r, g, b in q]
    return q

for fn in glob.glob('gidz/*.jpg'):
    i = Image.open(fn)
    i2 = ImageOps.fit(i, (256, 256))
    data = near_websafe(i2.getdata())
    i2.putdata(data)
    i2.save('op/' + fn)
