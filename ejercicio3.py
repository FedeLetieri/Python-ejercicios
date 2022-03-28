"""3) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:\n",
    "+  Mostrar la suma de dos números\n",
    "+  Mostrar la resta de dos números (el primero menos el segundo)\n",
    "+  Mostrar la multiplicación de dos números\n",
    "### Si ingresamos una opción inválida, el programa informará que es incorrecto"""



def menu():
    while True:
        print("A para mostra la suma de dos numeros")
        print("B para mostrar la resta de dos números (el primero menos el segundo)")
        print("C para mostrar la multiplicación de dos números")
        print("S para salir del programa")
        opcion=input("Elija una opcion: ")
        if (opcion=="S"):
            break
        return opcion
def programa():
    n1=int(input("Ingrese el primero numero: "))
    n2=int(input("Ingrese el segundo numero: "))

    opcion=menu()
    if (opcion=="A"):
      resultadoSuma=n1+n2
      print(int(resultadoSuma))  
    if (opcion=="B"):
       resultadoResta=n1-n2
       print(int(resultadoResta))
    if (opcion=="C"):
       resultadoMultiplicacion=n1*n2
       print(int(resultadoMultiplicacion))

programa()          