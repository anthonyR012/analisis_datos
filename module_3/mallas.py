
#las mallas de coordenadas son una representación gráfica de datos en un espacio bidimensional o tridimensional. 
# Estas mallas son comunes en la ciencia de datos, matemáticas y ingeniería para visualizar datos y realizar cálculos numéricos.


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5,0,10)
y = np.linspace(-5,5,10)

X, Y = np.meshgrid(x, y)

Z = np.sqrt(X**2 + Y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

plt.tight_layout()
plt.show()
