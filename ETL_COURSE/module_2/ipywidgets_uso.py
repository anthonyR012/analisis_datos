
import matplotlib.pyplot as plt
import pandas as pd
from ipywidgets import interact, widgets


# def f(x):
#     return print(f"El valor de x es: {x}")

# interact(f, x=0)

f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_Enero_comas.csv";

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True)

def grafica_serie(start, end):
    filtrado = cuerna[start:end]
    fig, ax = plt.subplots(figsize=(4,4))
    ax.plot(filtrado.To)
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Valor")

    plt.tight_layout()
    plt.show()

inicio_picker = widgets.DatePicker(description="Inicio", value=pd.to_datetime("2012-01-01"))
fin_picker = widgets.DatePicker(description="Fin", value=pd.to_datetime("2012-01-31"))

widgets.interactive(grafica_serie, start=inicio_picker, end=fin_picker)
