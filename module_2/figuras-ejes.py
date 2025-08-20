
import matplotlib.pyplot as plt
import pandas as pd

#fig y ax ( figura y ejes) 

# fig = plt.figure()
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# ax.plot([1, 2, 3], [1, 2, 3], 'k-')

# ax.set_title('title')
# ax.set_xlabel('x label')
# ax.set_ylabel('y label')

# ax.set_xlim(0, 4)
# ax.set_ylim(0, 4)

f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_Enero_comas.csv";

cuerna = pd.read_csv(f, index_col=0, parse_dates=True)

# plt.plot(cuerna.To) # es un plot de la variable To de la base de datos cuerna simple y rapido

fig, ax = plt.subplots()

ax.plot(cuerna.To, 'k-')


plt.tight_layout()
plt.show()

