

#utf8
# latin1
# ascii
# cp1252


#verifica el encoding de tu archivo antes de abrirlo

import pandas as pd
f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_1dia_comas_Encoding.txt"; #encoding ansi

data = pd.read_csv(f, encoding="cp1252") # o bien convertir el archivo a utf8

print(data)