

#Exportar graficos

import matplotlib.pyplot as plt  
import matplotlib.dates as mdates  
import pandas as pd
from dateutil.parser import parse

f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_Enero_comas.csv";

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True)

fig, ax = plt.subplots(figsize=(6,3))

f1 = parse("2012-01-10")
f2 = f1 + pd.Timedelta(days = 1)

ax.plot(cuerna.Ig, "r-",label="Ig")
ax.plot(cuerna.Ib, "k-",label="Ib")
ax.plot(cuerna.Id, "bo--",label="Id")

ax.legend()
ax.grid()
ax.set_xlim(f1 ,f2)

ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
ax.set_xlabel("Tiempo [mm-dd HH]")
ax.set_ylabel("Irradiancia $[W/m^2]$")
ax.set_title("Irradiancia en Cuernavaca")


# fig.savefig("/Users/anthonyrubio/Downloads/data/irradiancia.png", dpi=300)
 fig.savefig("/Users/anthonyrubio/Downloads/data/irradiancia.pdf", dpi=300)

plt.tight_layout()
plt.show()

