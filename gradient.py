red = (0xcc, 0x24, 0x1d)
aqua = (0x8e, 0xc0, 0x7c)

delta = (aqua[0] - red[0], aqua[1] - red[1], aqua[2] - red[2])

for i in range(10):
    color = list(red)
    color[0] = int(color[0] + (delta[0] * (i * 0.1)))
    color[1] = int(color[1] + (delta[1] * (i * 0.1)))
    color[2] = int(color[2] + (delta[2] * (i * 0.1)))
    print("[48;2;%d;%d;%dm  " % tuple(color), end="")
print("[48;2;%d;%d;%dm  " % aqua, end="")
print("[0m")
