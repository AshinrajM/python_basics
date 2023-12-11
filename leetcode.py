# 1672
# def rich(customer):
#     count = 0
#     for i in customer:
#         count1=0
#         for j in i:
#             count1+=j
#         if count1>count:
#             count=count1
#     return count


# a = [[1, 5], [7, 3], [3, 5]]
# result = rich(a)


# 412
# def fizz(number):
#     result = []
#     for i in range(1, number + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             result.append(str("FizzBuzz"))
#         elif i % 3 == 0:
#             result.append(str("Fizz"))
#         elif i % 5 == 0:
#             result.append(str("Buzz"))
#         else:
#             result.append(str(i))
#     return result

# print(fizz(6))


# 1342
# def sub(n, count=0):
#     if n % 2 == 0:
#         n = n / 2
#         count += 1
#         if n == 0:
#             return count
#         return sub(n, count)
#     else:
#         n = n - 1
#         count += 1
#         if n == 0:
#             return count
#         return sub(n, count)


# 383
# def sample(a,b):
#     for i in a:
#         if a.count(i) > b.count(i):
#             return False
#     return True

# print(sample('baa','aab'))



# from collections import Counter

# 136
# nums = [4,1,2,1,2]

# dict_nums=Counter(nums)

# for k,v in dict_nums.items():
#     if v==1:
#         print(k)