

import pandas as pd

f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_Enero_comas.csv";

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True)


columnas = cuerna.columns

# print(columnas)

nombres = {
    "Wd": "wind_direction",
    "Ws": "WindSpeed"
}

cuerna.rename(columns = nombres, inplace = True) # Renombrar columnas de un dataframe 

print(cuerna.columns)

viento = [columna for columna in cuerna.columns if "wind" in columna.lower()]
print(cuerna[viento])

