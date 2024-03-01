# 1 fns can be assigned to variables
def increment(num):
    return num + 4


f = increment  # here f refers to the same function object that increment refers to(f is like alias name for incremrent)
print(f(4))
# when we call f() python understands that f is referencing a fn and python executes
# that fn as it called directly. So, f(4) works exactly the same way the as increment(4), because f and icnrement
# referencing to same fn object
# fns can be assigned to variables that doesnt mean the returned value is stored in the variable.


# 2  fns can be returned from another function
def create_operation(operation):
    def func(a, b):
        if operation == "add":
            return a + b
        if operation=="multiply":
            return a*b
    return func
addition=create_operation('add')
print(addition(4,5))

