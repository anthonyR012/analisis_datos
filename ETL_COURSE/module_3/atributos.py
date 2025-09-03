


#Nivel de arreglo


import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(a.ndim)

#Shape


import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(a.shape)

#size


import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(a.size)

f = "/Users/anthonyrubio/Downloads/data/matriz10x10.txt";

m10x10 = np.loadtxt(f)

print(m10x10.ndim) #tiene dos dimensiones (numero de indices necesarios para acceder a cada elemento)

print(m10x10.shape) #tiene 10 filas y 10 columnas
 
print(m10x10.size) #tiene 100 elementos

