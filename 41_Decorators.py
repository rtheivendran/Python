
#Example1: Simple Function Decorator

def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper function executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print("Display function called....")

decorator_display = decorator_function(display)
decorator_display()


#Example 2: Simple Function Decorator

@decorator_function
def display():
    print("Display function called....")

display()


#Example 3: Simple Decorator for Function with arguments

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper function executed before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("display function called....")

@decorator_function
def display_info(name, age):
    print("display_info called with args {}, {}".format(name,age))


display()
display_info("Ramesh", 47)


#Example 4: Decorator with arguments

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, "Executed before {}".format(original_function.__name__))
            result =  original_function(*args, **kwargs)
            print(prefix, "Executed after {}".format(original_function.__name__))
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator("Testing >>>")
def display_info(name, age):
    print("display_info called with args {}, {}".format(name,age))

display_info("Ramesh", 47)
