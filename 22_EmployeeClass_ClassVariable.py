class Employee:

    #Class Variable
    raise_amount = 1.04
    employee_count = 0

    def __init__(self, first, last, pay=100000):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.employee_count +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def giveRaise(self):
        #self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)


print("No.of Employees = ", Employee.employee_count)

emp1 = Employee('Ramesh','Theivendran',50000);
emp2 = Employee('Aruna','Ramesh',50000);

print ("Employee class = {0}.".format(Employee.__dict__))
print()
print ("An Employee instance = {0}".format(emp1.__dict__))
print()

print(emp1.pay)
emp1.giveRaise()
print(emp1.fullname()," ",emp1.pay)
print ("emp1 instance = {0}".format(emp1.__dict__))
print()

#Giving a different raise to a employee by modifying a class variable for that instance
#This will not change the Class variable but makes a new instance member
emp2.raise_amount = 1.05
print(emp2.pay)
emp2.giveRaise()
print(emp2.fullname()," ",emp2.pay)

#Shows a new instance member is added to the instance
print ("emp2 instance = {0}".format(emp2.__dict__))
print()

#Shows the class members haven't changed for other instances and the class
print ("emp1 instance = {0}".format(emp1.__dict__))
print ("Employee class = {0}.".format(Employee.__dict__))
print()

print("No.of Employees = ", Employee.employee_count)


