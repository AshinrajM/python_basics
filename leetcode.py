from collections import Counter


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


# 136
# nums = [4,1,2,1,2]

# dict_nums=Counter(nums)

# for k,v in dict_nums.items():
#     if v==1:
#         print(k)


# 389
# s = "ae"
# t = "aea"

# for i in t:
#     if s.count(i)!=t.count(i):
#         res=i
# print(res)


# 268
# nums = [3,0,1]
# for i in range(len(nums)+1):
#     if i not in nums:
#         print(i)

# 448

# nums = [4,3,2,7,8,2,3,1]
# n=len(nums)
# n=len(nums)+1
# full=[x for x in range(1,n)]
# print(list(set(full)-set(nums)))


# 1903
# time limit exceeded for this code
# 1===>

# num = "5254"
# num1 = "35427"
# num2 = "4444"
# or
# 2==>
# n = 0
# odd = None
# for i in num2:
#     n = n * 10 + int(i)
#     if n % 2 != 0 and n > odd:
#         odd=n
# if odd is None:
#     print("")
# else:
#     print(str(odd))


# 1903
# b="3456586785678756456"
# indx = -1
# n = len(b)
# for i in range(n):
#     if int(b[i])%2 == 1:
#         indx = i

# if indx == -1:
#     print("")
# print(b[:indx+1])


# 2264
# num = "677713333999"
# num1 = "2400034"
# n = 0
# l = 0
# l1=0
# for i in range(len(num) - 2):
#     if num[i] == num[i + 1] == num[i + 2]:
#         if num[i] == "0":
#             l1="000"
#         n = (int(num[i]) * 100) + (int(num[i + 1]) * 10) + (int(num[i + 2]))
#     if n > l:
#         l = n

# if l > 0:
#     print(l)
# elif l1=="000":
#     print(l1)
# else:
#     print("abc")


# 1688

# def numberOfMatches(n,matches=0):
#     if n==1:
#         return matches
#     if n%2==0:
#         matches += n/2
#         n = n/2
#         return numberOfMatches(n,matches)
#     else:
#         matches += (n-1)/2
#         n = ((n-1)/2)+1
#         return numberOfMatches(n,matches)


