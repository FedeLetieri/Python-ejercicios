import pandas as pd


def resumen_cotizaciones(fichero):
    df = pd.read_csv(fichero, sep=';', decimal=',', thousands='.', index_col=0)
    ds=pd.DataFrame([df.min(), df.max(), df.mean()], index=['Mínimo', 'Máximo', 'Media'])
    return ds



hola=resumen_cotizaciones('cotizacion.csv')
print(hola)



