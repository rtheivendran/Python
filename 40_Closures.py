
#Example 1: Closure
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)
    return inner_function()

outer_function("Hello World")

#Example 2: Closure
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)
    return inner_function

fun1 = outer_function("Hello World")
fun2 = outer_function("Howdy...")

fun1()
fun2()


#Example 3: Closure
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

fun1 = outer_function("Hello World")
fun2 = outer_function("Howdy...")

fun1()
fun2()
