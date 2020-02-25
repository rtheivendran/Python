
#A class method takes cls as first parameter while a static method needs no specific parameters.
#A class method can access or modify class state while a static method can’t access or modify it.
# Class method are used to create factory methods. Factory methods return class object (similar to a constructor).
# Static methods are used to create utility functions.

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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    #Class method used as an alternative constructor
    @classmethod
    def from_string(cls, str):
        first, last, pay = str.split('-')
        return cls(first,last,int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Ramesh','Theivendran',50000);
emp2 = Employee('Aruna','Ramesh',50000);
emp3 = Employee.from_string("Vineha-Ramesh-100000")
emp4 = Employee.from_string('Vinusha-Ramesh-100000')

Employee.set_raise_amount(1.05)
emp1.set_raise_amount(1.08)
Employee.raise_amount = 100

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp3.giveRaise()
emp4.giveRaise()
print(emp3.fullname()," ",emp3.pay)
print(emp4.fullname()," ",emp4.pay)

import datetime
dt = datetime.date(2018,6,15)
print(Employee.is_workday(dt))

