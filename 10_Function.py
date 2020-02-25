
#def creates a function and assigns a name
#Arguments and return types are not declared
#All functions in Python return a value even if no return statement
#Special value None is returned if there is no return statement
#No function overloading
#Functions can be used as any other datatypes
    #Arguments to function
    #Return value of function
    #Assigned to variables
    #Items in tuples, lists e.t.c
#Mutable types are passed by reference
#immutable types are passed by value

print("\nExample 1:Simple function...\n")

# Function returning the sum
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    return total
total = sum(1000, 2000)
print("Sum : ", total)

def add (a,b,c=10,d=100):
    return a+b+c+d

print("Total : ", add(1,2))
print("Total : ", add(1,2,3,4))

def hello1(name):
    return "Hello " + name

print(hello1("Tom"))

#Default arugment
def hello2(greeting, name="Man"):
    return "{} {}".format(greeting, name)


print(hello2("Howdy", "Tom"))
print(hello2(name="Tom", greeting="Howdy"))
print(hello2("Howdy").upper())


def employee(name, role):
    return "{} is a {}".format(name, role)

#Positional arguments
print(employee("Charles", "FW developer"))

#Keyword arguments
print(employee(role="SW developer", name="Ramesh"))

print(employee("Steve", role="FW developer"))

#Positional argument cannot follow keyword argument
#print(employee(role="FW developer", "Mark"))

print("\nExample 2: Variable no.of arguments...\n")

def printargs(arg1, *vartuple):
    """This prints a variable passed arguments"""
    print(arg1)
    print("Variable arguments")
    print(type(vartuple))
    for var in vartuple:
        print(var)
    return


printargs(10)
printargs(70, 60, 50, 100)

print("\nExample 3: Variable no.of arguments and keyword arguments...\n")


def student_info(name, *args, **kwargs):
    print("name : ",name)
    print("args : ", args)
    print("kwargs : ", kwargs)


student_info('Ramesh', 'Math', 'Science', age=50, dept='Engg')

courses = ('Math', 'Science')
info = {'age': 50, 'dept': 'Engg'}

student_info('Ramesh', courses, info)
student_info('Ramesh', *courses, **info)


print("\nExample 4: Arguments of mutable types are passed by reference...\n")

# Pass by reference for Mutable types

def changeme(mylist):
    mylist.append([10, 20, 30, 40]);
    print("Values inside the function: ", mylist)
    return

def nochange(mylist):
    print("Address of mylist before = {}".format(hex(id(mylist))))
    mylist = mylist[1:-1];  # This would assign a  new reference in mylist
    print("Address of mylist after = {}".format(hex(id(mylist))))
    print("Values inside the function: ", mylist)
    return

list1 = [1, 2, 3, 4]
changeme(list1)
print("Values outside the function: ", list1)

list2 = [1, 2, 3, 4]
print("Address of list2 = {}".format(hex(id(list2))))
nochange(list2)
print("Values outside the function: ", list2)

print("\nExample 5: Arguments of immutable types are passed by value...\n")
# Pass by Value for immutable types

def printinfo(name, age=30):
    age += 10
    print("Name: ", name)
    print("Age ", age)
    return;

age = 40
printinfo(name="Ramesh")
printinfo(age=age, name="Aruna")
print("Age ", age)

print("\nExample 6: Anonymous functions...\n")

# Anonymous Function
#lambda argument_list: expression
product = lambda arg1, arg2: arg1 * arg2

# Now you can call the lambda function
print("Result: ", product(10, 20))
print("Result: ", product(20, 20))
