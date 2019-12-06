
# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
class Vehicle:
    #base superclass
    def __repr__(self):
        return f'<Vehicle>'

class GroundVehicle(Vehicle):
    #base class for ground vehicles
    def __repr__(self):
        return f'<GroundVehicle>'

class FlightVehicle(Vehicle):
    #baes class for flight vehicles
    def __repr__(self):
        return f'<FlightVehicle'

class Car(GroundVehicle):
    def __repr__(self):
        return f'<Car>'

class Motorcycle(GroundVehicle):
    def __repr__(self):
        return f'<Motorcycle>'

class Airplane(FlightVehicle):
    def __repr__(self):
        return f'<Airplane>'

class Starship(FlightVehicle):
    def __repr__(self):
        return f'<Starship>'


v = Vehicle()
g = GroundVehicle()
f = FlightVehicle()
c = Car()
p = Airplane()
s = Starship()
print(v,g,f,c,p,s)

vehicles = [v,g,f,c,p,s]
for veh in vehicles:
    print("Classname of instance: ", type(veh).__name__)




# print(type(v).__name__)  #printing out the name of of the class of the instance