#List Comprehensions

nums = [1,20,12,14,29,5,8,0,22,45,50,11,7]
print ("\nCopy a list with for loop...\n")
newlist =[]
for n in nums:
    newlist.append(n)
print (newlist)

print ("\nCopy a list with comprehension...\n")
newlist = [ n for n in nums ]
print (newlist)

print ("\nSquare elements in a list with comprehension...\n")
squaredlist = [ n*n for n in nums ]
print (squaredlist)

print ("\nOdd items in a list with comprehension...\n")
oddlist = [ n for n in nums if n%2 != 0 ]
print ("Odd items = ",oddlist)

# filter(function, list) offers an elegant way to filter out all the elements of a list,
# for which the function returns True. 
print ("\nEven items in a list using filter...\n")
evenlist = filter(lambda n: n%2 == 0, nums)
print ("Even items = ",evenlist)
for num in evenlist:
    print(num)

new_list = []
for letter in 'abcd':
    for num in range(4):
        new_list.append((letter,num))
print ("Newlist =",new_list)

new_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print ("Newlist =",new_list)


#Dictionary Comprehensions
print ("\nzip function.\n")
names = ['Jim','Bob','John','Dale']
teams = ['Software','Firmware','Radio','Sales']
managers = ['Tom','Ryan','Todd','Ron']
newList = []
for name, team, manager in zip(names, teams,managers):
    newList.append([name,team,manager])
print (newList)

print ("\nNew dictionary using for .\n")
new_dict={}
for name, team in zip(names, teams):
    new_dict[name] = team
print (new_dict)


print ("\nNew dictionary using dictionary comprehensions .\n")
new_dict = {name:team for name, team in zip(names, teams)}
print(new_dict)


print ("\nNew dictionary using dictionary comprehensions and condition .\n")
new_dict = {name:team for name, team in zip(names, teams) if name != 'Jim'}
print(new_dict)

#Set Comprehensions

print ("\nNew set using for .\n")
nums = [1,5,2,1,3,4,2,5,1,2,3,2,1,6,7,8,5,9,4,7,8,9,5,9]

new_set = set()
for n in nums:
    new_set.add(n)
print ("New set = ", new_set)

print ("\nNew set using set comprehensions .\n")
new_set = {n for n in nums}
print ("New set = ", new_set)


