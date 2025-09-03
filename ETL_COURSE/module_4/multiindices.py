
import pandas as pd
import matplotlib.pyplot as plt


f = "/Users/anthonyrubio/Downloads/data/Ti_blanco.csv";

Ti_b = pd.read_csv(f, index_col = 0, parse_dates = True)

f = "/Users/anthonyrubio/Downloads/data/Ti_negro.csv";

Ti_n = pd.read_csv(f, index_col = 0, parse_dates = True)


casos = pd.concat([Ti_b, Ti_n], axis=1, keys=["blanco", "negro"])

# fig, ax = plt.subplots()

# ax.plot(casos["blanco"], c="k")
# ax.plot(casos["negro"], c="r")

fig, ax = plt.subplots(figsize=(10,3))

# ax.plot(casos["blanco"]["Ti_C"], c="k")
# ax.plot(casos["negro"]["Ti_C"], c="r")

colores = casos.columns.levels[0]

for color in colores:
    ax.plot(casos[color]["Ti_S"], label=color)


mb = pd.MultiIndex.from_product([["blanco"],Ti_b.index],names=["C","fecha"])

Ti_bm = Ti_b
Ti_bm.index = mb

mn = pd.MultiIndex.from_product([["negro"],Ti_n.index],names=["C","fecha"])

Ti_nm = Ti_n
Ti_nm.index = mn


casos = pd.concat([Ti_bm, Ti_nm], axis=0)

print(casos.loc["blanco","2006-01-01"])
print("====")
print(casos.loc["negro","2006-01-01"])


# plt.tight_layout()
# plt.show()

