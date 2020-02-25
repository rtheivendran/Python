#Filter: filter(function,sequence)
#filter out all the elements of a sequence, for which the function returns True

from functools import partial, reduce

fib = [0,1,1,2,3,5,8,13,21,34,55]

odd_numbers = list(filter(lambda x: x % 2, fib))
print("Odd numbers: {}".format(odd_numbers))

even_numbers = list(filter(lambda x: x % 2 == 0, fib))
print("Even numbers: {}".format(even_numbers))

evener = partial(filter, lambda x:x%2 == 0)
print("Even numbers: {}".format(list(evener(fib))))


#Reduce: reduce(fuction, sequence)
#Continually applies the function to the sequence and returns a single value.

list1 = [10,20,30,40,50]
sum = reduce(lambda x,y: x+y, list1)
print("sum = {}".format(sum))

list1 = [10,40,12,324,545,31,1,111,2434,110]
max_list = reduce(lambda a,b: a if (a > b) else b, list1)
print("Max = {}".format(max_list))

n = 100
print("Sum of numbers from 1 to {} = {}".format(n, reduce(lambda x, y: x + y, range(1,n+1))))
