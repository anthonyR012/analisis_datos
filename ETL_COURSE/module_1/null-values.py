
#Valores nulos 
#miss

import pandas as pd
import missingno as ms
import matplotlib.pyplot as plt

f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_1dia_comas_Nans.csv";

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True) 

# print(cuerna.info()) # Información de los datos, tipe y nulos

f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_1dia_comas_NULOS.csv";

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True) 

# print(cuerna.head()) #Ahora no hay NaN

# print(cuerna.info()) # No identifica los nulos


#DEfinimos que valor tambien es nulo

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True, na_values = ["Nulo"]) 

# print(cuerna.info()) 

# ms.matrix(cuerna)

ms.bar(cuerna)

plt.show()