

import pandas as pd

f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_Enero_comas.csv";

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True)

# print(cuerna.loc["2012-01-02"]) # Localizar por fecha y hora 

# print(cuerna.loc["2012-01-02":"2012-01-17"]) # Localizar por rango de fechas 

# print(cuerna.Ig > 0) # Localizar por condicion

mascara = cuerna.Ig > 0

# print(cuerna.loc[mascara]) # Localizar por condicion

mascara = (cuerna.Ig > 0) & (cuerna.Ws != 0)

print(cuerna.loc[mascara])

#Tambien para reemplazar datos

cuerna.loc[mascara, "Ig"] = 0
