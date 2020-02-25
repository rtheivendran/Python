
import sys
#sys.path.append('/Users/rtheivendran')

#Import the whole module
import My_Module

#Import the whole module with an alias
import My_Module as myLib

#import all items from a module
#from My_Module import *

from My_Module import x, factorial, sumofnumbers

#import a specific item from a module with an alias
#from My_Module import factorial as fact

from My_Module import factorial as fact, sumofnumbers as sumnum

x = 25

try:
    print("Factorial of {} = {}".format(My_Module.x, My_Module.factorial(My_Module.x)))
    print("Sum of numbers upto {} = {}".format(My_Module.x, My_Module.sumofnumbers(My_Module.x)))

    print("Factorial of {} = {}".format(x, myLib.factorial(x)))
    print("Sum of numbers upto {} = {}".format(x, myLib.sumofnumbers(x)))

    print("Factorial of {} = {}".format(x, factorial(x)))
    print("Sum of numbers upto {} = {}".format(x, sumofnumbers(x)))

    print("Factorial of {} = {}".format(x, fact(x)))

    print("Sum of numbers upto {} = {}".format(x, sumnum(x)))

    print("System path {}".format(sys.path))

except ValueError as ex:
    print("Exception occurred: {}",ex)

