

import pandas as pd
import matplotlib.pyplot as plt

f = "/Users/anthonyrubio/Downloads/data/termopares/centro_cafeteria.csv"

Tcafe = pd.read_csv(f, index_col = 0, parse_dates = True)


f = "/Users/anthonyrubio/Downloads/data/termopares/exterior.csv"

Texterior = pd.read_csv(f, index_col = 0, parse_dates = True)

# Tcafe.plot(figsize=(10,3))
# Texterior.plot(figsize=(10,3),subplots=True)


#Limpieza Texterior (Tirar TMP5, datos < 0, renombrar columnas, resample promediado cada 10 min)

nombres = Texterior.columns.to_list()
nombres.remove("TMP5")

Texterior = Texterior[nombres]
mask = Texterior > 0
Texterior = Texterior[mask]

Texterior.columns = [nombre.replace("MP","") for nombre in nombres]

Texterior = Texterior.resample("10min").mean()

# Texterior.plot(figsize=(10,3))

#Limpieza Tcafe (Renombrar columnas, resample promediado cada 10 min)

nombres = Tcafe.columns.to_list()
Tcafe.columns = [nombre.replace("MP","") for nombre in nombres]

Tcafe = Tcafe.resample("10min").mean()

#Ambos conjuntos de datos de 12 a 5 pm

f = "/Users/anthonyrubio/Downloads/data/termopares/Text-12a17h.csv"

Texterior.loc["2023-04-04 12:00:00":"2023-04-04 17:00:00"].to_csv(f)

f = "/Users/anthonyrubio/Downloads/data/termopares/Tcafe-12a17h.csv"

Tcafe.loc["2023-04-04 12:00:00":"2023-04-04 17:00:00"].to_csv(f)



# plt.tight_layout()
# plt.show()

