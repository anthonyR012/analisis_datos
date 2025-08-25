
import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(A)
print("====")
print(B)

print("====")
print(np.dot(A,B)) #el producto punto es la multiplicacion de matrices cuadradas y de dimensiones iguales A * B = AB 

print("====")
print(np.transpose(A)) #transpuesta

print("====")
print(np.linalg.det(A)) #determinante

print("====")
print(np.linalg.inv(A)) #inversa

b = np.array([1,2])
x = np.linalg.solve(A, b) #solucion de sistemas de ecuaciones lineales
print("Valor de x: ", x)
# print(A + B)
# print(A - B)
# print(A * B)
# print(A / B)