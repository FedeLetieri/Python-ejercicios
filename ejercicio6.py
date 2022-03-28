" 1) Crea una superclase llamada Vehículo cuyos atributos sean Color y Ruedas. Redefine el método _str_"
"para que devuelva por pantalla:\n"
"> __Color: {El color del vehículo}, {Cantidad de ruedas} ruedas__. \n"
"### Crea una subclase llamada Carro y agrega los atributos Velocidad, Cilindraje. Redefine el método _str_ "
"para que devuelva por pantalla \n"
"> __Color: {El color del vehículo}, {Velocidad} Km/h, {Cantidad de ruedas} ruedas, {Cilindraje} cc\".__"

class vehiculos():
    "Metodos"
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas
    
    "metodo para llamar a la función"
    def __str__(self):
        return f"El color del vehiculos es {self.color} y tiene {self.ruedas} ruedas"

primerAuto=vehiculos("Negro",4)
print(primerAuto)

