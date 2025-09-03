

#valores nulos



import pandas as pd
import matplotlib.pyplot as plt  

f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_1dia_comas_Nans.csv";

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True) 


# print(cuerna.head)## contiene NaN en sus registros

# print(cuerna.dtypes) # Tippos de datos

# print(cuerna.nunique()) # Valors no unicos en cada columna

# print(cuerna.observacion.value_counts()) # Contar los valores unicos

# print(cuerna.isnull()) # regresa una tabla con true si es nulo

# print(cuerna.notnull()) # regresa una tabla con true si no es nulo

print(cuerna[cuerna.isnull()])

