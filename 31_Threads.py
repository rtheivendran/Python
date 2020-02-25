import time
import threading

def calc_square(numbers):
    print("Calculating square")
    for n in numbers:
        time.sleep(0.2)
        print("Square of {}= {}".format(n, n*n))


def calc_cube(numbers):
    print("Calculating cube")
    for n in numbers:
        time.sleep(0.2)
        print("Cube of {}= {}".format(n, n*n*n))


print("\nWithout any threads calling in sequence...")
list = [2,3,4,5,6,7,8,9]

start = time.time()
calc_square(list)
calc_cube(list)

print("We took {} seconds".format(time.time() - start))

print("\nTwo threads running in parallel...")
start = time.time()
t1 = threading.Thread(target=calc_square, args=(list,))
t2 = threading.Thread(target=calc_cube, args=(list,))

t1.start()
t2.start()

t1.join()
t2.join()
print("We took {} seconds".format(time.time() - start))
