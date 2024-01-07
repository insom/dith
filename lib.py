from PIL import Image, ImageOps
import sys
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

def average_buckets(buckets, topn):
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

def kmeans(bucket_count, data, verbose=False):
    topn = [random_color() for x in range(bucket_count)]
    for i in range(10):
        if verbose:
            for pixel in topn:
                print("[48;2;%d;%d;%dm  " % tuple(pixel), end="")
            print("[0m", end="")
            print(topn)
        topn = average_buckets(populate_buckets(data, topn), topn)
    return topn

def noisify_pixel(rgb, intensity):
    return [x * (1 + (random.random() * intensity)) for x in rgb]

def operate(filename, function, size=(256,256)):
    im = Image.open(filename)
    i2 = ImageOps.fit(im, size)
    data = i2.getdata()
    data = function(data)
    i2.putdata(data)
    i2.save('op/' + filename)
