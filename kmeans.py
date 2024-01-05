from PIL import Image, ImageOps
import math, random
from statistics import mean

def eu_distance(c1, c2):
    return math.sqrt(
        math.pow(c1[0] - c2[0], 2) +
        math.pow(c1[1] - c2[1], 2) +
        math.pow(c1[2] - c2[2], 2))

def random_color():
    r = int(random.random() * 255)
    g = int(random.random() * 255)
    b = int(random.random() * 255)
    return [r,g,b]

topn = [random_color() for x in range(4)]
im = Image.open('input.jpg')
i2 = ImageOps.fit(im, (150, 150))
data = i2.getdata()

def populate_buckets(image_data, topn):
    buckets = []
    for i in range(len(topn)):
        buckets.append([])
    for pixel in image_data:
        q = [[eu_distance(pixel, topn[i]), i] for i in range(len(topn))]
        q.sort()
        nearest_topn = q[0][1]
        buckets[nearest_topn].append(pixel)
    return buckets

def average_buckets(buckets):
    acc = []
    for i in range(len(topn)):
        bb = buckets[i]
        r = g = b = 0
        try: r = int(mean([x[0] for x in bb]))
        except: pass
        try: g = int(mean([x[1] for x in bb]))
        except: pass
        try: b = int(mean([x[2] for x in bb]))
        except: pass
        acc.append([r,g,b])
    return acc

for i in range(10):
    for pixel in topn:
        print("[48;2;%d;%d;%dm  " % tuple(pixel), end="")
    print("[0m", end="")
    print(topn)
    topn = average_buckets(populate_buckets(data, topn))
