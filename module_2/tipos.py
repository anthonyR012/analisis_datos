
# grafico plot (linea)
# grafico scatter (puntos)
# grafico bar (barras)
# grafico hist (histograma)
# grafico stem (stem)


import matplotlib.pyplot as plt  
import pandas as pd
from dateutil.parser import parse

f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_1dia_comas.csv";

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True)

fig, ax = plt.subplots()

ax.plot(cuerna.To)
ax.set_title('plot')

plt.tight_layout()
plt.show() 

ax.scatter(cuerna.To, cuerna.Ws)
ax.set_title('scatter')

plt.tight_layout()
plt.show() 

ax.bar(cuerna.To, cuerna.Ws)
ax.set_title('bar')

plt.tight_layout()
plt.show() 

ax.hist(cuerna.To)
ax.set_title('hist')

plt.tight_layout()
plt.show() 

ax.stem(cuerna.To)
ax.set_title('stem')

plt.tight_layout()
plt.show() 
