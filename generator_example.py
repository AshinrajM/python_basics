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
