import matplotlib.pyplot as plt  
import matplotlib.gridspec as gridspec
import pandas as pd
from dateutil.parser import parse


f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_Enero_comas.csv";

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True)

fig = plt.figure(figsize=(10,4))

gs = gridspec.GridSpec(2,2)

ax1 = fig.add_subplot(gs[0,:1])
ax2 = fig.add_subplot(gs[1,:1])
ax3 = fig.add_subplot(gs[1,1:])

ax1.plot(cuerna.To)
ax2.scatter(cuerna.To, cuerna.RH)
ax3.plot(cuerna.Ib)
ax3.plot(cuerna.Ig)
ax3.plot(cuerna.Id)

f1 = parse("2012-01-01")
f2 = f1 + pd.Timedelta(days = 1)

ax3.set_xlim(f1 , f2)

plt.tight_layout()
plt.show()