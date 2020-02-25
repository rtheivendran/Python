
#String is a immutable type
x =  "Hello"
y = x
print('Value of x = {} and address of x = {}'.format(x, hex(id(x))))
print('Value of y = {} and address of y = {}'.format(y, hex(id(y))))

y = "World"
print('Value of x = {} and address of x = {}'.format(x, hex(id(x))))
print('Value of y = {} and address of y = {}'.format(y, hex(id(y))))

x = x + y
y = x
z = 'Hello World'
zz = """ The best of both
Worlds."""

print('Value of x = {} and address of x = {}'.format(x, hex(id(x))))
print('Value of y = {} and address of y = {}'.format(y, hex(id(y))))
print('Value of z = {} and address of z = {}'.format(z, hex(id(z))))
print('Value of zz = {} and address of zz = {}'.format(zz, hex(id(zz))))


