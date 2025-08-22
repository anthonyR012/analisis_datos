

import matplotlib.pyplot as plt  
import pandas as pd

f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_Enero_comas.csv";

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True)

# print(cuerna.head())
fig, ax = plt.subplots()

# ax.scatter("To","RH",data=cuerna) # lo mismo pero pasando todo el dataframe
# ax.set_title('plot')

ax.plot(cuerna.Ig)
ax.plot(cuerna.Ib)
ax.plot(cuerna.RH)

plt.tight_layout()
plt.show()