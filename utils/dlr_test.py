from math import *
import sys

m, n = 5, 10

img = []
index = 0
for y in range(m):
    _ = []
    for x in range(n):
        _.append(hex(index)[-1])
        index += 1
    img.append(_)

for y in range(m):
    for x in range(n):
        print(img[y][x], end=" ")
    print()

angle = int(sys.argv[1])
alpha = radians(angle)

nrt = ceil(m * sin(alpha)) + n + 20
mrt = ceil(m * cos(alpha) + n * sin(alpha)) + 20
print(f"{nrt=}, {mrt=}")

rot = []
for y in range(mrt):
    _ = []
    for x in range(nrt):
        _.append(" ")
    rot.append(_)

x_offset = ceil(m * sin(alpha))

rise = n * sin(alpha)
run = n * cos(alpha)
max_start_y = ceil(m * cos(alpha))
fs = lambda y: y / tan(alpha + pi / 2)

y_incr = floor(n / rise)
x_incr = floor(n / run)

if y_incr > x_incr:
    mod_factor = y_incr // x_incr
    for line in range(max_start_y):
        a, b = ceil(fs(line)), line
        # how many times does it stack up in the x axis? (x_incr)
        # 5 / 4.33 = 1 times
        # how many times does it stack up in the y axis? (y_incr)
        # 5 / 2.5 = 2 times
        # this means, in every 2 iterations, y increases by 1, x increases by 2 itself
        # more generally, if x_incr/y_incr > 1, (x_incr/y_incr) can be treated as a mod factor wrt x and vice-versa
        # if y_incr > x_incr:
        #     mod_factor = y_incr // x_incr
        for pixel in range(n):
            # print(f"{(a + x_offset, b)} maps to {(pixel, line)}, i.e {img[line][pixel]}")
            rot[b][a + x_offset] = img[line][pixel]
            a += 1
            if pixel > 0 and pixel % mod_factor == 0:
                b += 1
        # print("----")
elif y_incr == x_incr:
    for line in range(max_start_y):
        a, b = ceil(fs(line)), line
        for pixel in range(n):
            rot[b][a + x_offset] = img[line][pixel]
            a += 1
            b += 1


for y in range(mrt):
    for x in range(nrt):
        print(rot[y][x], end=" ")
    print()
