import matplotlib.pyplot as plt
from math import *
import numpy as np

try:
    img = plt.imread("./assets/fish.png")
except FileNotFoundError:
    img = plt.imread("../assets/fish.png")

m, n = img.shape[:2]

angle = 10
alpha = (pi * angle) / 180

mrt = m + n                             # new image dimensions
nrt = mrt                               # new image dimensions
x_offset = ceil(m * sin(alpha))
fs = lambda y: y / tan(alpha + pi / 2)  # starting line equation

rot = np.zeros((mrt, nrt), dtype=img.dtype)

delta_x = cos(alpha)
delta_y = sin(alpha)

for i in range(ceil(m * cos(alpha))):
    x_, y_ = fs(i), i

    for px in range(n):
        try:
            x, y = round(x_), round(y_)
            rot[y, x + x_offset] = img[i, px]
            rot[y + 1, x + x_offset] = img[i, px]
            x_ += delta_x
            y_ += delta_y
        except IndexError:
            print(f"[index err] mapping {(x + x_offset, y)} to {(px, i)}")
            pass


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap="gray")

plt.subplot(1, 2, 2)
plt.title("Rotated Image")
plt.imshow(rot, cmap="gray")
plt.show()
