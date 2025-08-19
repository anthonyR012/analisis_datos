# En análisis de datos, una serie temporal es un conjunto de observaciones de una variable, 
# tomadas a lo largo del tiempo a intervalos regulares. Estos datos se organizan secuencialmente, mostrando cómo una variable cambia con el paso del tiempo. 

# Explicación más detallada:
# Observaciones ordenadas:
# Una serie temporal se caracteriza por el orden cronológico de sus observaciones. Cada punto de datos se asocia a un momento específico en el tiempo. 

# Intervalos regulares:
# Los datos se registran a intervalos constantes (por ejemplo, cada hora, día, semana, mes). 

# Variable única:
# La serie temporal se centra en el comportamiento de una única variable a lo largo del tiempo. 

# Análisis y predicción:
# El objetivo principal del análisis de series temporales es identificar patrones, tendencias y relaciones temporales en los datos para comprender el pasado y predecir el futuro. 

# Ejemplos de series temporales:
# Precios de acciones: El precio de una acción registrado diariamente a lo largo del tiempo. 
# Ventas mensuales: Las ventas de un producto registradas cada mes durante un año. 
# Temperatura diaria: La temperatura registrada cada día en un lugar específico. 
# Producción industrial: La producción de una fábrica medida mensualmente. 

# Importancia del análisis de series temporales:
# El análisis de series temporales es crucial en diversas disciplinas, incluyendo: 
# Finanzas: Para predecir precios de acciones, analizar tendencias del mercado.
# Economía: Para analizar el crecimiento económico, la inflación, el desempleo.
# Medicina: Para estudiar la evolución de enfermedades, el comportamiento de pacientes.
# Ingeniería: Para analizar el rendimiento de sistemas, predecir fallos.
# Meteorología: Para analizar patrones climáticos, predecir el tiempo.


import pandas as pd


# try:
#     with open("/Users/anthonyrubio/Downloads/data/Cuernavaca_1dia_comas.csv") as archivo:
#         content = archivo.read()
#         print(content)

# except FileNotFoundError:
#     print("No se encuentra el archivo") 

# try:
#     with open("/Users/anthonyrubio/Downloads/data/Cuernavca_T1dia_tabulador.csv") as archivo:
#         content = archivo.read()
#         print(content)

# except FileNotFoundError:
#     print("No se encuentra el archivo") 

a = pd.to_datetime("2020-01-01")
print("a: ", a)
a + pd.DateOffset(days=1)
print("a+pd.DateOffset(days=1): ", a + pd.DateOffset(days=1))