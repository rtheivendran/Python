
import sys

x = 10
print("Type of x {}".format(type(x)))
print("Size of x {}".format(sys.getsizeof(x)))

x = 1.5
print("Type of x {}".format(type(x)))
print("Size of x {}".format(sys.getsizeof(x)))

x = "Hello World"
print("Type of x {}".format(type(x)))
print("Size of x {}".format(sys.getsizeof(x)))

x = []
print("Type of x {}".format(type(x)))
print("Size of x {}".format(sys.getsizeof(x)))

x = ()
print("Type of x {}".format(type(x)))
print("Size of x {}".format(sys.getsizeof(x)))

x = {}
print("Type of x {}".format(type(x)))
print("Size of x {}".format(sys.getsizeof(x)))

x = set()
print("Type of x {}".format(type(x)),end=" ")
print("Size of x {}".format(sys.getsizeof(x)))


