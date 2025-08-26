import pandas as pd
import matplotlib.pyplot as plt

f = "/Users/anthonyrubio/Downloads/data/termopares/Tcafe-12a17h.csv";

Tcafe = pd.read_csv(f, index_col = 0, parse_dates = True)

f = "/Users/anthonyrubio/Downloads/data/termopares/Text-12a17h.csv";

Text = pd.read_csv(f, index_col = 0, parse_dates = True)

Ti = pd.concat([Tcafe, Text], axis=1, keys=["cafe", "exterior"])

fig, ax = plt.subplots(figsize=(10,3))

ax.plot(Ti["cafe"].mean(axis=1),"r.",label="cafe")
ax.plot(Ti["exterior"].mean(axis=1),"g.",label="exterior")
ax.legend()
ax.set_ylabel("Temp $[^oC]$")
ax.set_xlabel("Tiempo [mm-dd HH]")
ax.set_title("Temperaturas en Cuernavaca")

plt.tight_layout()
plt.show()