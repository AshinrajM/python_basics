# Decorator is a callable function or object  which can be used to modify a function


# Decorator function
def log_function_call(func):
    def wrapper(a, b):
        if b == 0:
            return "not divisible"
        result = func(a, b)
        return result

    return wrapper


# Applying the decorator
@log_function_call
def divide_numbers(a, b):
    print("division completed")
    return a / b


result = divide_numbers(3, 5)
print(f"Final result: {result}")

result2 = divide_numbers(3, 0)
print(f"Final result: {result2}")

# ===>    division completed                -1
#         Final result: 0.6                 -1
#         Final result: not divisible       -2

# here when we call divide number function with arguments 3,5 it goes to the function but due to a decorator
# is callled there this entire divide function is passed to the decorator function as argument.And it returns a
# wrapper function it accepts the the arguments of normal which is in argument of decorator function.Then it goes
# line by line and returns the "not divible" if the 2nd argument is 0. Otherwise  it calls the divide_numbers()
# (Because at the argument of decorator function our normal function is there).Then it divides the values and
# returns the results.As you can see we have provided a print() in the divide_numbers() before return.


add = lambda a, b: a + b
x = add(3, 7)
print("result:", x)
