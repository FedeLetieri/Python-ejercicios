""" Escribe una función que reciba un diccionario con las notas de los
alumnos de curso y devuelva una serie con la nota mínima, 
la máxima, media y la desviación típica de cada uno. """

import pandas as pd

def get_dicc(dicctionari):
    score_alumns=pd.Series(dicctionari)
    stadistics=pd.DataFrame([score_alumns.max(),score_alumns.min()
    ,score_alumns.mean(),score_alumns.std()],index=("Nota máxima",
    "Nota Minima","Nota media","Desviacion tipica"))
    return stadistics
    
    """  max_score=score_alumns.max()
    min_score=score_alumns.min()
    media_score=score_alumns.median()
    deviation_score=score_alumns.std() """

dicctionari = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5,'Federico': 10}
print(get_dicc(dicctionari))    