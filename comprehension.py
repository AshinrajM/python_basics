# list comprehension

# a = [1, 2, 3, 4, 5, 6, 78, 45]
# b = [i for i in a if i % 2 == 0]
# c = [i * i for i in a]

# print("c:", c)     ===>c: [1, 4, 9, 16, 25, 36, 6084, 2025]
# print("b:", b)     ===>[2, 4, 6, 78]

# new_list = ["python", "java", "javascript", "flutter", "php"]
# check = [i.upper() for i in new_list if i != "java"]
# latest = list(filter(lambda a: len(a) < 5, new_list))
# final = [i for i in range(5)]
# test = [i.replace("php", "golang") for i in new_list if len(new_list) > len(check)]


# print(test)          ===>['python', 'java', 'javascript', 'flutter', 'golang']
# print(final)         ===>[0, 1, 2, 3, 4]
# print(latest)        ===>['java', 'php']
# print(check)         ===>['PYTHON', 'JAVASCRIPT', 'FLUTTER', 'PHP']


# dictionary comprehension

# my_list1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# latest = {key.upper(): value for key, value in my_list1.items()}
# sample = {a: b * 3 for a, b in my_list1.items()}
# final = {key.replace("a", "H"): value * 3 for key, value in my_list1.items()}

# print(final)        ==>{'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
# print(sample)       ==>{'a': 3, 'b': 6, 'c': 9, 'd': 12, 'e': 15}
# print(latest)       ==>{'H': 3, 'b': 6, 'c': 9, 'd': 12, 'e': 15}


# list slicing

# a = "python-django"

# print(a[2:14])      ==>thon-django
# print(a[3:12:2])    ==>hndag
# print(a[:4])        ==>pyth
