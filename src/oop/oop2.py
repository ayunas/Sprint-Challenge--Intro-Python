# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle(object):  #explictly passing in object to remember where the Class object comes from
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels
    
    def drive(self):
        return "vroooom"
    
    def __repr__(self):
        return '<GroundVehicle>'

gv = GroundVehicle()

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__(2)
    
    def drive(self):
        return "BRAAAP!!"
    
    def __repr__(self):
        return '<Motorcycle>'


m = Motorcycle()
print('motorcycle wheels', m.num_wheels)



vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# # Go through the vehicles list and print the result of calling drive() on each.
for v in vehicles:
    print(v.drive())

#VSCode highlighted comments to flag to come back or whatever.
#FIXME
#BUG
#TODO
#XXX
