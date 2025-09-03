

import pandas as pd
import glob as glob

data = glob.glob("/Users/anthonyrubio/Downloads/data/esolmet/*")

f = "/Users/anthonyrubio/Downloads/data/esolmet/001.xlsx"

e1 = pd.read_excel(f, index_col=0,parse_dates=True,skiprows=[0,1,3,4])

f = "/Users/anthonyrubio/Downloads/data/esolmet/002.xlsx"

e2 = pd.read_excel(f, index_col=0,parse_dates=True,skiprows=[0,1,3,4])

e = pd.concat([e1,e2]) # Concatenar por filas

# e = pd.concat([e1,e2], axis=1) # Concatenar por columnas


df = pd.concat([pd.read_excel(archivo,index_col=0,parse_dates=True,skiprows=[0,1,3,4]) for archivo in data]) #Es posible que toque ordenarlos

df.sort_index(inplace=True) 






