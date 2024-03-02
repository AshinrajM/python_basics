# 1 fns can be assigned to variables
def increment(num):
    return num + 4


f = increment  # here f refers to the same function object that increment refers to(f is like alias name for incremrent)
# print(f(4))
# when we call f() python understands that f is referencing a fn and python executes
# that fn as it called directly. So, f(4) works exactly the same way the as increment(4), because f and icnrement
# referencing to same fn object
# fns can be assigned to variables that doesnt mean the returned value is stored in the variable.


# 2  fns can be returned from another function
def create_operation(operation):
    def func(a, b):
        if operation == "add":
            return a + b
        if operation == "multiply":
            return a * b

    return func


addition = create_operation("add")
# print(addition(4, 5))
# here when we are assigning a the function to the variable the variable will have an reference pointer to the entire
# function. So when addition is calling with values it also calls the create_operation with parameter , which means
# there will be access to those parameter because its in the memory space with function.


# 3 functions can be passed as arguments to another functions
def outer(og_fn):
    print("eneterd inner")
    def inner():
        return og_fn()

    return inner

def display():
    print("checkkkkk")

f = outer(display) # here we are passing a function as argument and it returns a function object of inner()
f() # here the stored inner function object calls the inner() and returns the fn which passed as an argument.

#output ==>
# eneterd inner
# checkkkkk