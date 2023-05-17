class Vehicle:
    licensecode = ""
    serialcode = ""
    face = ""
    def turnonairconditioner(self):
        print("Turn on : Air")

class Car(Vehicle):
    pass

class Pickup(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estadecar(Vehicle):
    pass

Car1 = Car()
Car1.turnonairconditioner()

Pickup1 = Pickup()
Pickup1.turnonairconditioner()

Van1 = Van()
Pickup1.turnonairconditioner()

Estadecar1 = Estadecar()
Estadecar1.turnonairconditioner()