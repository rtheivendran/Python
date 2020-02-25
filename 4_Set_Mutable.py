
#A set contains an unordered collection of unique and immutable objects
#sets can't contain mutable objects, sets are mutable

empty_list=[]
empty_list=list()

empty_tuple = ()
empty_tuple= tuple()

empty_set = {} #This will create a empty Dictionary
empty_set = set() #This will create a empty set
print(empty_set)

#Set doesn't support item assignment or indexing
#empty_set[0] = "Test"
empty_set.add("Test")
print(empty_set)

science_courses = {'Physics','Chemistry','Biology', 'Math', 'Computer Science'}
sc = science_courses
#Will create a new copy in memory
#sc = science_courses.copy()
#sc.clear()
print('Value of science_courses = {} and address of science_courses = {}'.format(science_courses, hex(id(science_courses))))
print('Value of sc = {} and address of sc = {}'.format(sc, hex(id(sc))))

art_courses = {'English', 'Art', 'Design'}
engg_courses = {'Civil','Mechanical','Electrical','Electronics','Computer Science'}

engg_courses.add('Math')
print(engg_courses)

print('Math' in science_courses)
print('Math' in art_courses)
print('Math' in engg_courses)

print("intersection : {} ".format( science_courses.intersection(engg_courses)))

print("Difference : {} ".format(science_courses.difference(engg_courses)))
print(engg_courses.difference(science_courses))

print(science_courses.union(engg_courses))
print("Union : {}".format(science_courses.union(engg_courses).union(art_courses)))

engg_courses.clear()
print(engg_courses)
