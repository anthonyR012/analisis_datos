


#FUNCION RESAMPLE DE FRECUENCIA

# resample es para hacer un resumen de los datos o ag
# En Pandas, resample() es un método utilizado para cambiar la 
# frecuencia de los datos de series temporales. Permite convertir datos de una
# frecuencia a otra, como de datos diarios a mensuales o de datos horarios a semanales.
# Es una herramienta útil para la manipulación y
# análisis de datos temporales, facilitando la agregación, reducción o aumento de la frecuencia de los datos. 


import pandas as pd
import matplotlib.pyplot as plt  

f = "/Users/anthonyrubio/Downloads/data/Temixco_2018_10Min.csv";

tmx = pd.read_csv(f, index_col = 0, parse_dates = True)

# print(tmx.info())

# tmx.loc["2018-03-10","To"].plot(figsize=(10,2), style="o")

# plt.tight_layout()
# plt.show() 

print(tmx.resample("h",closed="right").max())
