
class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

    def __str__(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        #super().__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

    def __str__(self):
        return super().__str__() + ", " +  self.staffnumber

p1 = Person("Ramesh", "Theivendran")
emp1 = Employee("Aruna", "Ramesh", "1000")

print(p1.Name())
print(emp1.GetEmployee())

print(p1)
print(emp1)