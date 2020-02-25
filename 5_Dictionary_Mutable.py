
#Dictionaries: Key:Value mapping type
#Keys can be any immutable type
#Values can be of any type
#Dictionaries can store values of different types

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

print(dict)
print (dict['one'] )      # Prints value for 'one' key
print (dict[2]   )        # Prints value for 2 key

tinydict = {'name': 'John','code':6734, 'dept': 'sales', 'age' : 47}
print (tinydict)
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values
print (tinydict.items())  # Print all items in the dictionary

print (tinydict.get('name')) #Get value for key
print (tinydict.get('phone'))
print (tinydict.get('phone','Not Found'))

#adding a new key
tinydict['phone'] = '(831) 430 0701'

#updating a key/value
tinydict['name']= 'Jim'
tinydict['age'] = 50
print (tinydict)

#updating multiple items
tinydict.update({'name':'Bob','age':50,'phone':'(831)111-1111'})
print (tinydict)

#Removing an item from Dict using pop or del
#x = tinydict.pop('age')
del tinydict['age']
print (tinydict)

user =  {
    'username' :'tramesh',
    'first': 'ramesh',
    'last':'theivendran',
    'age': '48',
}

print("\nIterating through a Dict...\n")

for key, value in user.items():
    print ("Key: " + key)
    print ("Value: " + value)


print("\nIterating through a Dict...\n")
for key in user.keys():
    print ("Key: " + key)
    print ("Value: " + user[key])


print("\nGoing over the keys...\n")

for k in user.keys():
    print("key: " + k )

print("\nGoing over the values...\n")

for v in user.values():
    print("value: " + v)

print("\nList in a Dictionary...\n")

favorite_languages = {
    'ramesh' : ['C','C++','Python','golang','Swift','Kotlin',"C#",'Java'],
    'aruna' : ['C','C++'],
    'vineha' : ['Java', 'Python'],
    'vinusha' :['Python', 'R']
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s Favourite languages are:")
    for language in languages:
        print("\t" + language.title())


print("\nDictionary in a Dictionary...\n")

users = {
    'Ramesh': {
        'first': 'ramesh',
        'last': 'theivendran',
        'address': '203 bean creek road, Unit I',
        'city': 'scotts Valley',
        'state': 'ca',
        'zip': '95066',
    },
    'Aruna': {
        'first': 'aruna',
        'last': 'ramesh',
        'address': '203 bean creek road, Unit I',
        'city': 'scotts Valley',
        'state': 'ca',
        'zip': '95066',
    },
    'Rathika': {
        'first': 'rathika',
        'last': 'theivendran',
        'address': 'no 7 mariappa nadar lane',
        'city': 'tirumangalam',
        'state': 'tamil nadu',
        'zip': '626706',
    },
}

for username, userinfo in users.items():
    print("\nUser Name: " + username)
    full_name = userinfo['first'] + " " + userinfo['last']
    full_address = "{0}\n\t\t{1}\n\t\t{2}\n\t\t{3}".format(userinfo['address'], userinfo['city'], userinfo['state'].upper(),
											   userinfo['zip'])

    print("\nFull name : " + full_name.title())
    print("Address : " + full_address.title())


print("Done with Dictionary...")

