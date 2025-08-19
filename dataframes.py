

#Panda convierte todas las estructuras a dataframes

import pandas as pd


f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_To_1dia_comas.csv";

cuerna = pd.read_csv(f) #cuerna es un dataframe

# print(cuerna)
#print(cuerna.index) #indices del dataframe ( Los indices son las filas)



cuerna = pd.read_csv(f, index_col = 0, parse_dates = True) #cuerna es un dataframe con indices de fecha y hora 

# print(cuerna)


#indice = identificador unido de las filas

# print(cuerna.resample("D").mean()) #promedio diario de las columnas del dataframe cuerna 

# print(cuerna.resample("ME").mean()) #promedio mensual de las columnas del dataframe cuerna


#objeto tiempo en pandas


f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_1dia_comas.csv";

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True) #cuerna es un dataframe con indices de fecha y hora 

print(type(pd.to_datetime("2025-01-01"))) # convierte una cadena de texto a un objeto de tipo datetime


a = pd.to_datetime("2025-01-01") + pd.DateOffset(years=1)
# print(a) # 2026-01-01


period = pd.Period("2025-01-01", freq="D", month=2)
# print(period) # 2025-01-01

delta = pd.to_datetime("2025-01-01 12:00") + pd.Timedelta("1h")
# print(delta) # 2025-01-01 13:00



print(cuerna.columns) # imprime los nombres de las columnas
print("=====================")
print(cuerna.To) # imprime la columna To
print("=====================")
print(cuerna[["To", "Ws"]]) # imprime las columnas To y Ws
print("=====================")
print(cuerna.iloc[0]) # imprime la primera fila
print("=====================")
print(cuerna.iloc[0:10]) # imprime las primeras 10 filas
print("=====================")
print(cuerna.iloc[-1]) # imprime la ultima fila
print("=====================")
print(cuerna.iloc[-1:-10:-1]) # imprime las ultimas 10 filas



