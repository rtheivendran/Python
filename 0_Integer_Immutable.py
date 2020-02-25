

#Integer is a immutable type
x =  10
y = x
print('Value of x = {} and address of x = {}'.format(x, hex(id(x))))
print('Value of y = {} and address of y = {}'.format(y, hex(id(y))))

y = 11
print('Value of x = {} and address of x = {}'.format(x, hex(id(x))))
print('Value of y = {} and address of y = {}'.format(y, hex(id(y))))

x = x + 1
z = 11

print('Value of x = {} and address of x = {}'.format(x, hex(id(x))))
print('Value of y = {} and address of y = {}'.format(y, hex(id(y))))
print('Value of z = {} and address of z = {}'.format(z, hex(id(z))))

z = z +1
print('Value of z = {} and address of z = {}'.format(z, hex(id(z))))

