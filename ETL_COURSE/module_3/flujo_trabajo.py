
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import glob as glob



vels = glob.glob("/Users/anthonyrubio/Downloads/data/obstacle/*")
vels.sort()

def transforma_imagen(imagen):
    img = Image.open(imagen)
    img = np.array(img)
    img = img[:,:,:3]

    return img

# img = transforma_imagen(vels[0])
# img1 = transforma_imagen(vels[1])

# fig, ax = plt.subplots(3)
# ax[0].imshow(img[:, :, 0])
# ax[1].imshow(img[:, :, 1])
# ax[2].imshow(img[:, :, 2])


# rojas = np.dstack(img[:,:,0], img1[:,:,0])
# azules = np.dstack(img[:,:,1], img1[:,:,1])
# verdes = np.dstack(img[:,:,2], img1[:,:,2])

# lista = []
# for vel in vels:
#     lista.append(transforma_imagen(vel)[:, :, 0])

# rojas = np.dstack(lista)


rojas = np.dstack([transforma_imagen(vel)[:, :, 0] for vel in vels])
verdes = np.dstack([transforma_imagen(vel)[:, :, 1] for vel in vels])
azules = np.dstack([transforma_imagen(vel)[:, :, 2] for vel in vels])

fig, ax = plt.subplots()

ax.imshow(rojas[:, :, 0])
# ax.imshow(verdes)
# ax.imshow(azules)

plt.tight_layout()
plt.show()


#guardar datos en un archivo

# np.save("/Users/anthonyrubio/Downloads/data/rojas.npy", rojas)
# np.save("/Users/anthonyrubio/Downloads/data/verdes.npy", verdes)
# np.save("/Users/anthonyrubio/Downloads/data/azules.npy", azules)

#cargar datos de un archivo

# rojas = np.load("/Users/anthonyrubio/Downloads/data/rojas.npy")
# verdes = np.load("/Users/anthonyrubio/Downloads/data/verdes.npy")
# azules = np.load("/Users/anthonyrubio/Downloads/data/azules.npy")

