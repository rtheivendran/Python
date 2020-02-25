# Simple function to return exponential
def exp(base, power):
    return base ** power

def two_to_the(power):
    return 2 ** power

print("Value exp(2,10) = {}".format(exp(2, 10)))
print("Value two_to_the(10) = {}".format(two_to_the(10)))
print("two_to_the type is {}".format(type(two_to_the)))

print("\n Example 1: Partial to create a new function from an existing function\n")
# Use partial to create a new function
from functools import partial

two_to_the = partial(exp, 2)
print("Value two_to_the(10) = {}".format(two_to_the(10)))

print("partial type is {}".format(type(partial)))
print("two_to_the type is {}".format(type(two_to_the)))

square_of = partial(exp, power=2)
print("Value square_of(10) = {}".format(square_of(10)))

cube_of = partial(exp, power=3)
print("Value cube_of(10) = {}".format(cube_of(10)))

ten_power_two = partial(exp, base=10, power=2)
print("Value ten_power_two() = {}".format(ten_power_two()))

print("\n Example 2: Map alternative to list comprehensions\n")

list1 = [1, 2, 3, 4]
square_list = [square_of(x) for x in list1]
print("Squared list = {}", format(square_list))

# Same as above but using map
# map(function, sequence)
square_list = map(square_of, list1)
print("Squared list = {}", format(list(square_list)))

fun_square = partial(map, square_of)
square_list = fun_square(list1)
print("Squared list = {}", format(list(square_list)))

print("\n Example 3: Map alternative to list comprehensions\n")


def fahrenheit(T):
    return ((float(9) / 5) * T + 32)


def celsius(T):
    return (float(5) / 9) * (T - 32)


temperatures = [36.5, 37, 37.5, 38, 39]

temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))

print(temperatures_in_Fahrenheit)
print(temperatures_in_Celsius)

F = list(map(lambda x: (float(9) / 5) * x + 32, temperatures))
print(F)
C = list(map(lambda x: (float(5) / 9) * (x - 32), F))
print(C)

print("\n Example 3: Map with multiple list\n")

a = [10, 20, 30, 40]
b = [17, 12, 11, 10]
c = [-1, -4, -5, -9]
print(list(map(lambda x, y, z: x + y + z, a, b, c)))

print("\n Example 4: Complicated Map \n")

#Write a Python program, which returns a list with 2-tuples.
#Each tuple consists of a the order number and the product of the price per items and the quantity.
#The product should be increased by 10 if the value of the order is less than $100

orders = [["34587", "Learning Python", 4, 40],
          ["98762", "Programming Python", 5, 55],
          ["77226", "Head First Python", 3, 30],
          ["88112", "Python3", 3, 25]]

min_order = 100
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10),
                          map(lambda x: (x[0], x[2] * x[3]), orders)))

print(invoice_totals)
