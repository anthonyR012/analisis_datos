
import numpy as np

m = np.arange(15)

print(m)

m = m.reshape(3, 5) # 3 filas y 5 columnas, reshape es para cambiar el tamaño de un arreglo de una sola dimension a uno de dos dimensiones o viceversa
print("====")
print(m)

m = np.random.randint(0,10,(3,3))
print("====")
print(m.reshape(-1)) # -1 es para que se adapte al tamaño del arreglo original (desdoblar el arreglo en un vector)

m = np.random.rand(100,100,3)
print("====")
print(m)

n = m.reshape(-1,3)
print("====")
print(n.shape)

np.resize(m, (10,2))
print("====")
print(m)