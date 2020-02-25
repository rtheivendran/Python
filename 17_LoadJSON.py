import json

with open('./Data/devices.json') as f:
    data = json.load(f)

print(type(data))
print("\nIterating through a Dict keys...\n")
for key in data.keys():
   print ("Key: " + key)

print()
print("Phones....")
i = 1
for device in data['phones']:
   print("Phone {}: {} ships with {} Operating system".format(i , device['name'], device['os']))
   i+=1

print()
print("Watches....")
i = 1
for device in data['watches']:
    print ("Watch {}: {} ships with {} Operating system".format(i, device['name'], device['os']))
    i +=1

print("\nIterating through a Dict keys and values...\n")
for key in data.keys():
    print("{}....".format(key))
    i = 0
    for dev in data[key]:
        print (dev)


