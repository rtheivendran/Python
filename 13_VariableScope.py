# Variable Scope: Local, Enclosed, Global, Build-ins (LEGB)
# Python statements: global and nonlocal

#1.The innermost scope is searched first and it contains the local names
#2. The scopes of any enclosing functions, which are searched starting with the nearest enclosing scope
#3. The next-to-last scope contains the current module's global names
#4. The outermost scope, which is searched last, is the namespace containing the built-in names

# Example 1:
print("\n\nExample 1 to show variable scopes: Local, Enclosed and Global")
x = 'global x'

def outerFunction():
    x = 'outer x'

    def innerFunction():
        x = 'inner x'
        print(x)

    innerFunction()
    print(x)

# Call outerFunction
outerFunction()
print(x)

# Example 2:
print("\n\nExample 2 to show variable scopes: Local, Enclosed and Global")

x = 0

def outer():
    x = 1

    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


# Call outer
outer()
print("global:", x)


# Example 3: global keyword
#global keyword to read and write a global variable inside a function.
print("\n\nExample 3 to show use of global statement")
x = 0

def outer():
    x = 1

    def inner():
        global x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


# Call outer
outer()
print("global:", x)


# Example 4: nonlocal keyword
# nonlocal means "not a global or local variable." So it changes the identifier to refer 
# to an enclosing method's variable.
print("\n\nExample 4 to show use of nonlocal statement")
x = 0

def outer():
    x = 1

    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)


# Call outer
outer()
print("global:", x)
