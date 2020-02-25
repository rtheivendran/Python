class Employee:

    def __init__(self, first, last, pay=100000):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Ramesh','Theivendran');
emp2 = Employee('Aruna','Ramesh')

print(emp1.fullname())
print(emp2.fullname())

print(Employee.fullname(emp1))
print(Employee.fullname((emp2)))
print ("emp1 instance = {0}".format(emp1.__dict__))
print()
print ("Employee Class = {0}".format(Employee.__dict__))