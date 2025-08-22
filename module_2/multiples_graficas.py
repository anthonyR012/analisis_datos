import matplotlib.pyplot as plt  
import pandas as pd
from dateutil.parser import parse

f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_Enero_comas.csv";

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True)

fig, ax = plt.subplots(2, figsize=(10,3), sharex=True, sharey=True)

f1 = parse("2012-01-18")
f2 = f1 + pd.Timedelta(days = 3, hours = 12)

ax[0].plot(cuerna.Ig, label="Ig")
ax[0].plot(cuerna.Id, label="Id")
ax[0].plot(cuerna.Ib, label="Ib")
ax[1].plot(cuerna.Ig, label="Ig")
ax[1].plot(cuerna.Id, label="Id")
ax[1].plot(cuerna.Ib, label="Ib")

ax[0].set_xlim(f1 , f2)
ax[0].grid()
ax[0].legend()
ax[0].set_xlabel("Tiempo [mm-dd HH]")
ax[0].set_ylabel("Radiación $[W/m^2]$")
ax[0].set_title("Radiación solar en Cuernavaca")

plt.tight_layout()
plt.show()