"### Crea una clase llamada _Rectangulo_ con dos puntos (inicial y final) que formarán la diagonal del rectángulo.\n",
"+ Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.\n",
"+ Añade al rectángulo un método llamado Mostrar_base que muestre la base.\n",
"+ Añade al rectángulo un método llamado Mostrar_altura que muestre la altura.\n",
"+ Añade al rectángulo un método llamado Mostrar_area que muestre el area."


class rectangulo():
    def __init__(self,puntoInicial=None,puntoFinal=None):
        self.puntoIncial=puntoInicial   

