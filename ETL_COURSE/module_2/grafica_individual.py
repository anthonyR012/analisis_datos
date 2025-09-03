

import matplotlib.pyplot as plt  
import pandas as pd


f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_1dia_comas.csv";

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True)

plt.plot(cuerna.To)


plt.tight_layout()
plt.show()
