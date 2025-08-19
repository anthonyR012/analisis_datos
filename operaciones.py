
import pandas as pd

df = pd.read_csv('/Users/anthonyrubio/Downloads/data/Cuernavaca_1dia_comas.csv', index_col = 0, parse_dates = True)


# print(df.To.mean()) # Promedio

# print(df.To.median()) # Mediana

# print(df.To.mode()) # Moda

# print(df.To.min()) # Minimo

# print(df.To.max()) # Maximo

# print(df.To.std()) # Desviacion estandar

# print(df.To.var()) # Varianza

# print(df.To.sum()) # Suma

# print(df.To.prod()) # Producto

# print(df.To.cumsum()) # Suma acumulada

# print(df.To.cumprod()) # Producto acumulado

# print(df.To.cummin()) # Minimo acumulado

# print(df.To.cummax()) # Maximo acumulado

# print(df.To.diff()) # Diferencia

# print(df.To.pct_change()) # Porcentaje de cambio

# print(df.To.skew()) # Coeficiente de asimetria

# print(df.To.kurt()) # Coeficiente de curtosis

# print(df.To.corr()) # Correlacion

# print(df.To.cov()) # Covarianza


# print(df.To - df.To.mean()) # Restar la media de la columna To de cuerna

df["To_avg"] = df.To.mean() # Agregar la columna To_avg
print(df) 
del df["To_avg"] # Borrar la columna To_avg

# df.drop(columns = ["To_avg", "Ws_avg", "Wd_avg", "P_avg"]) # Borrar varias columnas