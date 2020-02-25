#Tuple is immutable list

tuple = ('bob', 'phil' , 'mark', 'tom', 'sam', 'adam')
tuple1 = tuple
print('Value of tuple = {} and address of tuple = {}'.format(tuple, hex(id(tuple))))
print('Value of tuple1 = {} and address of tuple1 = {}'.format(tuple1, hex(id(tuple1))))

# Cannot change a tuple
#tuple[2]='jim'

tuple = tuple[1:4]
print('Value of tuple = {} and address of tuple = {}'.format(tuple, hex(id(tuple))))
print('Value of tuple1 = {} and address of tuple1 = {}'.format(tuple1, hex(id(tuple1))))

tinytuple = ('bill', 'john')

print (tuple)              # Prints complete list
print (tuple[0] )          # Prints first element of the list
print (tuple[0:])          # Prints first to last element
print (tuple[1:3])         # Prints elements starting from 2nd till 3rd
print (tuple[2:])          # Prints elements starting from 3rd element
print (tinytuple * 2)      # Prints list two times
print (tuple + tinytuple)  # Prints concatenated lists


print(sorted(tuple))

#iterating through a tuple
print("iterating a tuple..")
for name in tuple:
	print(name)

print("iterating a tuple..")
for name in sorted(tuple):
	print(name)

#tuples can have items of different types
t = (1,2,3,4,5,6)
print('Value of tuple = {} and address of tuple = {}'.format(t, hex(id(t))))
print('Value of tuple = {} and address of tuple = {}'.format(t, hex(id(t[0]))))
print('Value of tuple = {} and address of tuple = {}'.format(t, hex(id(t[1]))))


#Conver tuple to a list
ls = list(t)
print(ls)

