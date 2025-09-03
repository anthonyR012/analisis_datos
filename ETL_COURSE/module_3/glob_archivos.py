

import glob as glob

result = glob.glob("/Users/anthonyrubio/Downloads/data/*.csv")
# result = glob.glob("/Users/anthonyrubio/Downloads/data/*")
# result = glob.glob("/Users/anthonyrubio/Downloads/data/Cuerna*.csv")
# result = glob.glob("/Users/anthonyrubio/Downloads/data/?uerna*") Lo que tenga la cadena y empice con un caracter 
# result = glob.glob("/Users/anthonyrubio/Downloads/data/**/*") Trae contenido de data y sus subcarpetas 

# print(result)

imgs = glob.glob("/Users/anthonyrubio/Downloads/data/obstacle/*")
imgs.sort()
for img in imgs:
    print(img)