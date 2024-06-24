import matplotlib.pyplot as plt
from math import *
import numpy as np

try:
    img = plt.imread("./assets/fish.png")
except FileNotFoundError:
    img = plt.imread("../assets/fish.png")

m, n = img.shape[:2]

angle = 120
alpha = (pi * angle) / 180

mrt = m + n                                         # new image dimensions
nrt = mrt                                           # new image dimensions                                       
x_offset = ceil(m * sin(alpha))
fs = lambda y: y / tan(alpha)                       # starting line equation

rot = np.zeros((mrt, nrt), dtype=img.dtype)

delta_x = sin(alpha)
delta_y = cos(alpha)

for i in range(ceil(n * sin(alpha))):
    x_, y_ = fs(i), i
    
    for px in range(m):
        try:
            x, y = round(x_), round(y_)
            rot[y, x + x_offset] = img[px, i]
            rot[y + 1, x + x_offset] = img[px, i]
            x_ -= delta_x
            y_ += delta_y
        except IndexError:
            print(f"[index err] mapping {(x + x_offset, y)} to {(i, px)}")
            pass


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap="gray")

plt.subplot(1, 2, 2)
plt.title("Rotated Image")
plt.imshow(rot, cmap="gray")
plt.show()