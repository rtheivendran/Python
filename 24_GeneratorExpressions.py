
#Function to return square of items in a list
def square_numbers(nums):
    res = []
    for i in nums:
        res.append(i*i)
    return res

nums= [1,2,3,4,5]

print (square_numbers(nums))

#Generator Expressions

def square_numbers_generator(nums):
    for n in nums:
        yield n*n

gen = square_numbers_generator(nums)

print ("Generator ", gen)
print ("Generated val",next(gen))
print ("Generated val",next(gen))
print ("Generated val",next(gen))
print ("Generated val",next(gen))
print ("Generated val",next(gen))
#print ("Generated val",next(gen))

gen = square_numbers_generator(nums)
#Iterate through a generator expression
for i in gen:
    print (i)

#Another way to define a generator
gen = (n*n for n in nums)
print("Printing generator as a list ",list(gen))

gen = (n*n for n in nums)
for i in gen:
    print (i)


