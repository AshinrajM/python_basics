# 1  These are some of the basic built in functions in python

# to check the data type
# a=78
# print(type(a))

# slicing
# a='python'
# print(a[2:4])

# lower and upper
# a='python'
# b='DJANGO'
# print(a.upper(),b.lower())

# strip used to remove white spaces from the beginning or at the end
# a='   python,django,abc  '
# b=a.strip()
# print(a)
# print(b)

# replace
# a='python'
# print(a.replace('n','c'))

# split is used to split a string into a list
# list() can create list with each letters as elemets in string
# a = "python"
# print(a.split()) ==> ['python']
# print(list(a))  ==>  ['p', 'y', 't', 'h', 'o', 'n']

# format can be used to combine two datatypes
# a = 40
# b = "python{}"
# print(b.format(a)) ==>python40  here {} is the placeholder

# range returns a sequence of numbers
# a=5
# for i in range(a):
#     print(i)      ==> 0 1 2 3 4


# 2 List []
# List are mutable while are strings are immutables

# append
# a = []
# for i in range(5):
#     a.append(i)
# print(a) #[0, 1, 2, 3, 4]

# clear() clears the elements from the list but list exists
# a.clear()
# print(a)    ==> []

# insert - adding as an element

# a=[]
# for i in range(5):
#     a.append(i,input('enter element'))  i is the index position here
# print(a)    ==>[3,4,5,6,4]


# pop
# a = [1, 3, 4, 5, 6]
# a.pop()
# print(a)    ==>[1, 3, 4, 5]

# extend
# my_list = [1, 2, 3]
# my_list.extend([4, 5, 6])
# print(my_list)  ==>[1, 2, 3, 4, 5, 6]

# remove
# my_list = [1, 2, 3, 2]
# my_list.remove(2)  Removes the first occurrence of 2
# print(my_list) ==> [1, 3, 2]

# index
# my_list = [1, 2, 3, 4, 5]
# print(my_list.index(3)) ==> 2

# count
# my_list = [1, 2, 3, 2, 3, 2, 3, 2]
# print(my_list.count(2))  # Returns the number of occurrences of 2 here it is 4

# reverse
# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()
# print(my_list)  ==>[5, 4, 3, 2, 1]


# 3 Tuple ()
# when a tuple is created we can't add or remove elements but  we can convert it into list

# a=(1,2,3,45,6,"python")
# print(a) ==> (1, 2, 3, 45, 6, 'python')

# tuple to list
# my_tuple = (3,4,5,6,"python")
# my_list=list(my_tuple)
# print(my_list)      ==>[3, 4, 5, 6, 'python']

# list to tuple
# my_list = (2, 3, 4, 5, 6)
# my_tuple = tuple(my_list)
# print(my_tuple)     ==>(2, 3, 4, 5, 6)

# 3 dictionary {'': }
# in dictionary elements are stored in key-value format,duplicates are not allowed in dictionaries

# 1==>  my_dict={'brand':'W','year':2023,'price':450005,'brand':'Y'}
#       print(my_dict)  ==>{'brand': 'Y', 'year': 2023, 'price': 450005} duplicates are not allowed so the last value assigned will be displayed

# 2==>  thisdict = dict(name = "John", age = 36, country = "Norway")
#       print(thisdict)       ==> using dict() constructor also we can create dictionaries


# adding elements
# 1==>  thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
#       thisdict["color"] = "red"
#       print(thisdict) ==>   {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
# 2==>  print(dict(thisdict, owner="usman")) ==>{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red', 'owner': 'usman'}
# 3==>  thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
#       thisdict.update({"tyres": "fresh"})
#       print(thisdict) ==>{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'tyres': 'fresh'}


# update values by using key
# 1==>   thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# t      hisdict["year"] = 2018
#        print(thisdict)     ==>{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
# 2==>   thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
#        thisdict.update({"year": 2020})
#        print(thisdict)     ==>{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# pop()
# thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# thisdict.pop("model")
# print(thisdict)     ==>{'brand': 'Ford', 'year': 1964}

# popitem()
# thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "color": "red"}
# thisdict.popitem()
# print(thisdict)     ==>{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# del()
# thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# del thisdict["model"]
# print(thisdict)     ==>{'brand': 'Ford', 'year': 1964}
# del thisdict        ==>Entire dictionary can be deleted using del command


# 4 Set {}
# A set is a collection which is unordered, unchangeable*, and unindexed:but you can remove items and add new items.
# Also duplicates are not allowed in sets

# add()
# set1 = {"apple", "banana", "cherry"}
# set1.add("abcd")
# print(set1)     ==>{'abcd', 'banana', 'apple', 'cherry'}

# update() - add from another set
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# remove()
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

# discard()     - the difference with remove is that discard wont raise an error if the element doesnt exist but remove does.
# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)


# lambda - anonymous fn
# Its a small function that can take n number of arguments but can have only one expression

# 1  add = lambda a, b: a + b
#   x = add(3, 7)
#   print("result:", x)


# 2    def add(a, b):
#       result = a + b
#       subtract = lambda x, y: x - y
#       return {"subtract": subtract(a, b), "addition": result}


# a = add(6, 2)
# print("result:", a)     ===>result: {'subtract': 4, 'addition': 8}
