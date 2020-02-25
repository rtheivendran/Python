
#List is Mutable

list = [1, 5, 10, 15, 8, 12, 7,2 ]
list1 = list
print('Value of list = {} and address of list = {}'.format(list, hex(id(list))))
print('Value of list1 = {} and address of list1 = {}'.format(list1, hex(id(list1))))

#Can modify a list item as they are mutable
list[0]= 4
print('Value of list = {} and address of list = {}'.format(list, hex(id(list))))
print('Value of list1 = {} and address of list1 = {}'.format(list1, hex(id(list1))))

list = list[1:4]
print('Value of list = {} and address of list = {}'.format(list, hex(id(list))))
print('Value of list1 = {} and address of list1 = {}'.format(list1, hex(id(list1))))

tinylist = [123, 100]

print (list)            # Prints complete list
print (list[0] )        # Prints first element of the list
print (list[-1] )       # Prints last element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd
print (list[2:] )       # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists and create a new list in memory

print("Max = ",min(list))
print("Mix = ",max(list))
print("Sum = ",sum(list))

subjects = ['Physics','Math','Biology','Computer Science','Chemistry']
print(subjects)

print(subjects.index('Chemistry'))

print('Math' in subjects)

new_subjects = ['History','Geography','Art']
new_subjects.insert(0,'English')
new_subjects.append('Electronics')
print(new_subjects)

#Append takes a singleton as argument
print(len(subjects))
subjects.append(new_subjects)
print("Value of subjects after append = {}".format(subjects))
print(len(subjects))

#Extend takes a list as an argument
subjects.extend(new_subjects)
print("Value of subjects after extend = {}".format(subjects))
print(len(subjects))


cars = ["acura","honda","toyoto","lexus","benz","bmw","nissan","infinity"]
print(cars)

#append an item to end of the list
cars.append("tesla")
print(cars)

#pop an item from end of the list
print(cars.pop())

#insert at the begining of a list
cars.insert(0,"tesla")
print(cars)

#remove an item from the list
cars.remove('tesla')
print(cars)

#sort a list
cars.sort(reverse=True)
print("Sorted cars = ", cars)

# returns a sorted list
print(sorted(cars))

#List to a string
car_str = ' - '.join(cars)
print(car_str)
print(car_str.split(' - '))

#iterating through a list
print("iterating a list...")
for car in cars:
	print( car )

print("iterating a list...")
for index, car in enumerate(cars, start=1):
	print( index, car )

print("iterating using index...")
for i in range(len(cars)):
	print(cars[i])

print("poping elements from a list...")
for i in range(len(cars)):
	print(cars.pop())

#Convert list to a tuple
tu = tuple(subjects)
print (tu)

print('Done with List...   ')
