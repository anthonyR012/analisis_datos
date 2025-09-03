
import matplotlib.pyplot as plt  
import numpy as np
from PIL import Image


f = "/Users/anthonyrubio/Downloads/data/python.png";

img = Image.open(f)
# img.show()


fig = np.array(img)
# print(fig.shape)

alpha = fig[:,:,3]
# print(alpha.shape)

red = fig[:,:,0]
# print(red.shape)

green = fig[:,:,1]
# print(green.shape)

blue = fig[:,:,2]
# print(blue.shape)

# plt.imshow(alpha)
# plt.show()

# fig, ax = plt.subplots()
# a = ax.imshow(alpha, cmap='gray')
# fig.colorbar(a)

fig, ax = plt.subplots(4, figsize=(10,12))

a = ax[0].imshow(alpha, cmap='gray')
b = ax[1].imshow(red, cmap='gray')
c = ax[2].imshow(green, cmap='gray')
d = ax[3].imshow(blue, cmap='gray')

fig.colorbar(a)
fig.colorbar(b)
fig.colorbar(c)
fig.colorbar(d)

plt.tight_layout()
plt.show()