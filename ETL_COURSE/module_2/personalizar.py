

import matplotlib.pyplot as plt  
import pandas as pd
from dateutil.parser import parse


f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_Enero_comas.csv";
cuerna = pd.read_csv(f, index_col = 0, parse_dates = True)
f1 = parse("2012-01-01")
f2 = f1 + pd.Timedelta(days = 1)

fig, ax = plt.subplots(figsize=(10,4))

ax.plot(cuerna.Ig,"r-",label="Ig")
ax.plot(cuerna.Ib,"k-",label="Ib")
ax.plot(cuerna.Id,"bo--",label="Id")

ax.set_xlim(f1 , f2)
ax.grid()
ax.legend()
ax.set_xlabel("Tiempo [mm-dd HH]")
ax.set_ylabel("Radiación $[W/m^2]$")
ax.set_title("Radiación solar en Cuernavaca")

plt.tight_layout()
plt.show()
