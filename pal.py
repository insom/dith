import sys
from lib import *

def generate_palette():
    red = (0xcc, 0x24, 0x1d)
    aqua = (0x8e, 0xc0, 0x7c)
    delta = (aqua[0] - red[0], aqua[1] - red[1], aqua[2] - red[2])
    res = []
    for i in range(10):
        color = list(red)
        color[0] = int(color[0] + (delta[0] * (i * 0.1)))
        color[1] = int(color[1] + (delta[1] * (i * 0.1)))
        color[2] = int(color[2] + (delta[2] * (i * 0.1)))
        res.append(tuple(color))
    return res

def palettize(data):
    buckets = kmeans(8, data)
    buckets = generate_palette()
    new_data = []
    for pixel in data:
        pixel = noisify_pixel(pixel, 0.3)
        q = [[eu_distance(pixel, buckets[i]), i] for i in range(len(buckets))]
        q.sort()
        nearest_bucket = q[0][1]
        new_data.append(tuple(buckets[nearest_bucket]))
    return new_data

if __name__ == '__main__':
    operate(sys.argv[1], palettize)
