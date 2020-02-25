
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        Vehicle.name = "Charles's Lexus"
        self.MSPR = "100000"
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle()
car1.name = "Benz"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Honda"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

print(car1.description())
print(car2.description())

print ("car1 instance = {0}".format(car1.__dict__))
print()
print ("car2 instance = {0}".format(car2.__dict__))
print()
print ("Vehicle Class = {0}".format(Vehicle.__dict__))
