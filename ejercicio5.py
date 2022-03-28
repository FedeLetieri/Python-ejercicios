"PARTE 1:"
"Crea una clase llamada _Punto_ con sus dos coordenadas X y Y.\n",
"+ nAñade un método constructor para crear puntos, si no se recibe una coordenada, su valor será cero.\n"
"+ Redefine el método string para que al imprimir por patalla el punto aparezca en formato (X,Y)\n"
"+ Define el método Cuadrante que indique a qué cuadrante pertenece el punto:"
"******************************************************************************************************************************"
"PARTE 2 :"
"### Crea una clase llamada _Rectangulo_ con dos puntos (inicial y final) que formarán la diagonal del rectángulo.\n",
"+ Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.\n"
"+ Añade al rectángulo un método llamado Mostrar_base que muestre la base.\n"
"+ Añade al rectángulo un método llamado Mostrar_altura que muestre la altura.\n"
"+ Añade al rectángulo un método llamado Mostrar_area que muestre el area."
"******************************************************************************************************************************"
import math

class Punto():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        'print("Se creo un punto")'

    
    def __str__(self):
         return f"({self.x},{self.y})"

    def seleccionDeCuadrantes(self):
        if(self.x>=0 and self.y>=0):
            print(f"{self}Pertenece al cuadrante A")
        elif(self.x<=0 and self.y>=0):
            print(f"{self}Pertenece al cuadrante B")
        elif(self.x<=0 and self.y<=0):
            print(f"{self}Pertenece al cuadrante C")
        else:
            print(f"{self}Pertenece al cuadrante D")    

    def vector(self,otroPunto):        
        vectorEntreDosPuntosEnX=self.x - otroPunto.x
        vectorEntreDosPuntosEnY=self.y - otroPunto.y
        return print(f"El vector entre los dos puntos es ({vectorEntreDosPuntosEnX},{vectorEntreDosPuntosEnY})")



class rectangulo():
    def __init__(self,puntoInicial=Punto(0,0) , puntoFinal=Punto(0,0)):
        self.puntoInicial=puntoInicial   
        self.puntoFinal=puntoFinal
        self.base=abs(puntoInicial.x-puntoFinal.x)
        self.altura=abs(puntoInicial.y-puntoFinal.y)   
        self.area=self.base*self.altura   

    def mostrarBase(self):
         print(f"La base del rectangulo es {self.base}")

    def mostrarAltura(self):
         print(f"La altura del rectangulo es {self.altura}")

    def mostrarArea(self):
         print(f"El area del rectangulo es {self.area}")

    

"EJECUCION:"
coordenadaA=Punto(0,-2)
coordenadaB=Punto(-3,-1)
coordenadaC=Punto(3,-4)    
def PuntoA():
    coordenadaA.seleccionDeCuadrantes()
    coordenadaB.seleccionDeCuadrantes()
    coordenadaB.vector(coordenadaA)
"Ejecucion Segunda Parte"
def puntoB():   
    primerRectangulo=rectangulo(coordenadaA,coordenadaC)
    primerRectangulo.mostrarBase()
    primerRectangulo.mostrarAltura()
    primerRectangulo.mostrarArea()

PuntoA()    