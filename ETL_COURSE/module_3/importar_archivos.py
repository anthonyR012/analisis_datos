

#loadtext = carga de archivos de texto (simples y uniformes)
#loadcsv = carga de archivos csv
#loadexcel = carga de archivos excel

#getfromtext = carga de archivos de texto (complejos)
#getfromcsv = carga de archivos csv
#getfromexcel = carga de archivos excel


import numpy as np

f = "/Users/anthonyrubio/Downloads/data/matriz3x3.txt";

m3x3 = np.loadtxt(f)

# print(m3x3)
print("========")
# print(m3x3[0,1])


f = "/Users/anthonyrubio/Downloads/data/matriz10x10.txt";

m10x10 = np.loadtxt(f)

print("========")
# print(m10x10)

f = "/Users/anthonyrubio/Downloads/data/matriz10x10.txt";

m10x10 = np.genfromtxt(f)

# print("========")
# print(m10x10) 


#Cual es la ventaje entre genfronmtxt y loadtxt

f = "/Users/anthonyrubio/Downloads/data/matriz3x3_comment02.txt";

m3x3 = np.loadtxt(f, comments="--") #ignorar las lineas que comienzan con #

print(m3x3)

f = "/Users/anthonyrubio/Downloads/data/matriz3x3_comment02.txt";

m3x3 = np.genfromtxt(f, comments="--") #ignorar las lineas que comienzan con --

print(m3x3)

f = "/Users/anthonyrubio/Downloads/data/matriz3x3_faltantes.txt";

m3x3 = np.genfromtxt(f) #marca los faltantes con NaN
#podemos definir en vez de NaN el valor que queremos que tome 

print(m3x3)

# f = "/Users/anthonyrubio/Downloads/data/matriz3x3_faltantes.txt";

# m3x3 = np.genfromtxt(f, missing_values=0)


# print(m3x3)

