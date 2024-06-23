import matplotlib.pyplot as plt
from math import *
import numpy as np

try:
    img = plt.imread("./assets/fish.png")
except FileNotFoundError:
    img = plt.imread("../assets/fish.png")

m, n = img.shape[:2]

angle = 60
alpha = (pi * angle) / 180

mrt = m + n                                         # new image dimensions
nrt = mrt                                           # new image dimensions                                       
x_offset = ceil(m * sin(alpha))
fs = lambda x: tan(alpha) * x                       # starting line equation

rot = np.zeros((mrt, nrt), dtype=img.dtype)

delta_x = 1 / sin(alpha)
delta_y = 1 / cos(alpha)

for i in range(floor(n * sin(alpha))):
    x_, y_ = i, fs(i)
    
    for px in range(m):
        try:
            x, y = round(x_), round(y_)
            rot[y, x + x_offset] = img[px, i]
            rot[y + 1, x + x_offset + 1] = img[px, i]
            rot[y + 2, x + x_offset + 2] = img[px, i]
            rot[y + 3, x + x_offset + 3] = img[px, i]
            x_ -= delta_x
            y_ += delta_y
        except IndexError:
            pass


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap="gray")

plt.subplot(1, 2, 2)
plt.title("Rotated Image")
plt.imshow(rot, cmap="gray")
plt.show()