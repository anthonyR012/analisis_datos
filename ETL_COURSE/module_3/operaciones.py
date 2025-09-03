
#arreglo multidimensional


import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a)

#np.eye = crea una matriz identidad
#np.zeros = crea una matriz de ceros
#np.ones = crea una matriz de unos

print(np.zeros((3,3)))
print("====")
print(np.ones((3,3)))
print("====")
print(np.eye(3))
print("====")
print(np.full((3,3), -1))
print("====")
print(np.random.rand(3,3))
print("====")
print(np.random.randint(0,10,(3,3)))


#elementos basicos artimeticos

unos = np.ones((3,3))
azar = np.random.randint(1,3,(3,3))

print("====")
print(unos + azar)
print("====")
print(unos - azar)
print   ("====")
print(unos * azar)
print   ("====")
print(unos / azar)

