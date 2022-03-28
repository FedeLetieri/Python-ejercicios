""""Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros no se cobran hasta finales de año y se te suman al balance final de tu cuenta de ahorros. 
Escribe un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros.
 El programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer año. 
 Redondea cada cantidad a dos decimales"""

#def cuenta_ahorros():
dineroDepositado = int(input())
#def calculo_interes(dineroDepositado):
interesAnual=0.04 
#dineroTotal=0
año=["Primer","Segundo","Tercero"]
for i in range(0,3):
  dineroDepositado += dineroDepositado*interesAnual
  print(f"El dinero total del {año[i]} año es: ",round(float(dineroDepositado),2))

#cuenta_ahorros()           
#calculo_interes(dineroDepositado)    