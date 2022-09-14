# Crear una función con tres parámetros que sean números que se suman entre sí.

""" Crear una clase coche.
Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
Una función que incremente el número de puertas que tiene el coche.
Crear un objeto miCoche en el main y añadirle una puerta.
Mostrar el número de puertas que tiene el objeto """


class Coche ():

    puertas = 2

    def incrementarPuertas(self):
        self.puertas += 1


miCoche = Coche()

print(f"el coche tiene: {miCoche.puertas} puertas ")

miCoche.incrementarPuertas()

print(f"Incrementamos las puertas del coche ahora son: {miCoche.puertas }")
