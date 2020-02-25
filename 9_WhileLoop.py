
# Perform a task n times
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# Sum of "n" Numbers
sum = 0
count = 0
n = 5
while count <= n:
    sum = sum + count
    count += 1
print ("Sum numbers up to ", n, " = ", sum)


# Sum of "n" Numbers using while...else
sum = 0
count = 0
n = 5
while count <= n:
    sum = sum + count
    count += 1
else:
    print ("Sum numbers up to ", n, " = ", sum)


# Sum of "n" Numbers
sum = 0
count = 0
n = 5
while True:
    sum = sum + count
    count += 1
    if count > n:
        break;
print ("Sum numbers up to ", n, " = ", sum)
