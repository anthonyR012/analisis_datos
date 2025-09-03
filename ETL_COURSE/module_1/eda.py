
# El Análisis Exploratorio de Datos, o AED, es un paso importante en cualquier proyecto
#  de Análisis de Datos o Ciencia de Datos. El AED consiste en investigar el conjunto de datos para
# descubrir patrones y anomalías (valores atípicos) y formular hipótesis basadas en nuestra comprensión del conjunto de datos.

# El análisis de datos de elementos de datos (EDA) implica generar estadísticas resumidas para los datos numéricos del
# conjunto de datos y crear diversas representaciones gráficas para comprenderlos mejor.
# En este artículo, comprenderemos el análisis de datos de elementos de datos (EDA) 
# con la ayuda de un conjunto de datos de ejemplo. Para ello, utilizaremos el lenguaje Python ( biblioteca Pandas ).

# En este artículo, descubrirá la importancia del análisis de datos exploratorios (EDA) en la ciencia de datos
# y explorará cómo las estadísticas y técnicas exploratorias ayudan a visualizar datos exploratorios para obtener conocimientos más profundos.

import pandas as pd
import matplotlib.pyplot as plt  

f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_1dia_comas.csv";

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True) 

# cuerna.plot(subplots=True)
print(cuerna.columns)
columns =  ['To', 'Ws', 'Wd', 'P']

cuerna[columns].plot(subplots=True)

plt.tight_layout()
plt.show() 


