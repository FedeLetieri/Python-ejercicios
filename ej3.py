""" Escribe una función que reciba los datos siguientes en un DataFrame,
una lista de meses, y devuelva el balance (ventas - gastos) 
total en los meses indicados.
datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 
'Ventas':[30500, 35600, 28300, 33900], 
'Gastos':[22000, 23400, 18100, 20700]} """

import pandas as pd

datos_2022 = {'Mes   ':['Enero', 'Febrero', 'Marzo', 'Abril'],
              'Ventas':[30500, 35600, 28300, 33900],#datos en un dicctionario  
              'Gastos':[22000, 23400, 18100, 20700]} 
             
def balance(datos):
    new_balance=pd.DataFrame(datos)
    return new_balance


balance_2022=balance(datos_2022)
print(balance_2022)