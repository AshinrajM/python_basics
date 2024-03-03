# Generator in python is a function that returns an iterator which produces a sequences of values when iterated over.
# Generators are useful when we want to produce a large sequence of values but we dont want to store all of them.
# instead return there will be "yield"


def powers_of_two():
    n = 1
    while True:
        yield n
        n *= 2

# Using the generator
gen = powers_of_two()
for _ in range(5):
    print(next(gen))

# In this example, powers_of_two is a generator function that yields the next power of 2 each time it's called.
# It doesn't return all the powers of 2 at once but generates them one by one using the yield keyword.


# 1 fibonacci series using generator


# def fib():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, b + a


# f = fib()
# for _ in range(10):
#     print(next(f))


# 2 factorial of numbers

# def factorial():
#     a = 0
#     result = 1
#     while True:
#         yield result
#         a += 1
#         result *= a


# fact = factorial()
# for _ in range(10):
#     print(next(fact))


# 3 vowels identifier generator from a strings


# def vowels(word):
#     vowels = "aeiouAEIOU"
#     for i in word:
#         if i in vowels:
#             yield i


# word = input("Enter the word")
# v = vowels(word)
# for i in v:
#     print(i)
