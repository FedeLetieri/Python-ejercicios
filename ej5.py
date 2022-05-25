""" El archivo comercio_interno.csv contiene información sobre el comercio interno desde la década del 90.
Escribe un programa que:
a. Muestre por pantalla las dimensiones del Data Frame, el número de datos que contiene,
los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas.
b. Muestre por pantalla un gráfico de los datos de empleo por provincia y su relación con la columna valor.
c. Muestre por pantalla la columna alcance_nombre ordenada alfabéticamente.
d. Muestre un gráfico de la actividad_producto_nombre agrupados en relación al valor
e. Sume por alcance_nombre los valores de los años 2009 al 2019
f. Muestre un gráfico de la actividad_producto_nombre en la provincia de Mendoza del año 2015 al 2019 """


from os import sep
import pandas as pd

def get_list(lista): #Obtiene un archivo csv w
    df=pd.read_csv(lista,index_col=0,sep=',',)#sep=',',index_col=0
    stadistics=pd.DataFrame([df])#Lo devuelve como data Frame
    return stadistics

datos=get_list("comercio.csv")
print(datos)    