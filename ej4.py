""" El archivo autos.xlsx contiene datos de precios de autos
y stock. Construye el código necesario que emita
el precio mínimo, el máximo y promedio. """

import pandas as pd
import glob

def get_list_excel(lista):#Obtiene una tabla excel y emite el max,min y promedio
    info=pd.read_excel(lista)
    stadistics=pd.DataFrame([info.max(),info.min(),info.mean()],index=("Maximo","Minimo","media"))
    return stadistics






list_transform=get_list_excel('14.autos.xlsx')
print(list_transform)   