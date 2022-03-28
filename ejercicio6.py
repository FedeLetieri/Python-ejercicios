" 1) Crea una superclase llamada Vehículo cuyos atributos sean Color y Ruedas. Redefine el método _str_"
"para que devuelva por pantalla:\n"
"> __Color: {El color del vehículo}, {Cantidad de ruedas} ruedas__. \n"
"### Crea una subclase llamada Carro y agrega los atributos Velocidad, Cilindraje. Redefine el método _str_ "
"para que devuelva por pantalla \n"
"> __Color: {El color del vehículo}, {Velocidad} Km/h, {Cantidad de ruedas} ruedas, {Cilindraje} cc\".__"


"********************************************************************************************************"
class vehiculos():
    "Metodos"
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas
    
    "metodo para llamar a la función"
    def __str__(self):
        return f"El color del vehiculos es {self.color} y tiene {self.ruedas} ruedas"


"********************************************************************************************************"
"PRIMERA SUBCLASE DE VEHICULO"
class carro(vehiculos):
    """ def __init__(self,velocidad,cilindraje):
        self.velocidad=velocidad
        self.cilindraje=cilindraje """
    velocidad=0
    cilindraje=0

    def __str__(self):
        return f"Color:{self.color}\n"\
               f"Velocidad: {self.velocidad} km/h\n"\
               f"Ruedas:{self.ruedas}\n"\
               f"Cilindraje:{self.cilindraje} cc\n"    
"********************************************************************************************************"
class camioneta(vehiculos):
    carga=0
    def __str__(self):
        return f"Color:{self.color}\n"\
               f"Ruedas: {self.ruedas} km/h\n"\
               f"Carga:{self.carga}kg\n"







"Ejecucion:"
print("Primer Vehiculo:")
primerAuto=vehiculos("Negro",4)
print(primerAuto)
"Ejecucion:"
print("\nSegundo vehiculo:")
segundoAuto=carro("Gris",4)
segundoAuto.velocidad=150
segundoAuto.cilindraje=40
print(segundoAuto)                
"Ejecucion:"
print("\nTercer Vehiculo:")
tercerAuto=camioneta("Blanco",6)
camioneta.carga=500
print(tercerAuto)