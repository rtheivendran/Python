
for i in range(10):
    i += 2
    print("Value of i for loop = ",i)

i = 0
while (i < 10):
    i+= 2
    print("Value of i in while loop = ", i)

#Iterating through a list
print ("Iterating through a list")
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)


print ("Iterating through a range of integers")
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

print ("Iterating through a range of integers")
# Prints out 3,4,5
for x in range(3, 6):
    print(x)

print ("Iterating through a range of integers with increments")
# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)


print ("Sum of n numbers")
# Prints out the sum 0+1+2+....n
n = 5
sum = 0
for x in range(n+1):
    sum = sum + x
print(sum)

print ("Sum of n numbers with a for...else")
# Prints out the sum 0+1+2+....n
n = 5
sum = 0
for x in range(n+1):
    sum = sum + x
else:
    print(sum)


print ("Odd numbers up to n")
# Prints out only Odd numbers up to n
n =10
for x in range(n+1):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)


print ("Continue statement skips the iteration and continues with the loop")
for letter in 'Vineha_Ramesh':
   if letter == 'h':
      continue
   print ('Current Letter :', letter)


print ("Break statement break a loop")
for letter in 'Vineha_Ramesh':
   if letter == 'h':
      break
   print ('Current Letter :', letter)

print ("Pass statement executes the pass block")
for letter in 'Vineha_Ramesh':
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)



print ("Print all even number and stop when you see 237")
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number == 237:
      break
    else:
        if number % 2 == 0:
            print(number)

#Print a NxM matrix
print ("Printing a NxM matrix")
num_rows = 4
num_cols = 5

for x in range(num_rows):
    print ('*', end=" ")
    for y in range(num_cols-1):
        print ('*', end=" ")
    print()
print('')
