"""Desarrolla un programa que permita leer 2 valores y que
 emita por pantalla la suma, la resta, el producto, la
  división, el resto, el promedio y el doble producto del
   primero menos la mitad del segundo."""


def ingreseNumeros():
    numero1=int(input("Ingrese el primero numero: "))
    numero2=int(input("Ingrese el segundo numero: "))
    return numero1,numero2

def suma(numero1,numero2):
    resultadoSuma=numero1+numero2
    return print("El resultado de la suma es ",resultadoSuma)

#numeros=(7,2)
ingreseNumeros()
resultado=suma(ingreseNumeros)
print(resultado) 