
# csv = Comma Separated Values
# xlsx = Microsoft Excel


import pandas as pd

# read csv with pandas

f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_1dia_comas.csv";

cuerna = pd.read_csv(f)


print(type(cuerna))

cuerna = pd.read_csv(f, index_col = 0, parse_dates = True)


#read xlsx with pandas

f = "/Users/anthonyrubio/Downloads/data/Cuernavaca_To_1dia_comas.xlsx";

cuerna = pd.read_excel(f)

# print(cuerna)

#Parametros utilies de read_csv

f = "/Users/anthonyrubio/Downloads/data/Cuernavca_T1dia_tabulador.csv";

cuerna = pd.read_csv(f, sep = "\t") #separador por tabulador

print(cuerna)

cuerna = pd.read_csv(f,
            sep = "\t",
            header=None,
            skiprows=1,
            names=["tiempo", "temperatura"],
            index_col=0,
            parse_dates=True) #separador por tabulador y salta la primer fila

print(cuerna.head)
