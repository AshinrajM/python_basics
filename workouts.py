

# Q1 => sort it appropriate the number in each word in string
# values="from3 ashin2 kannur4 iam1"

# new_values=values.split()
# for i in range(len(new_values)):
#     new_values[i]=new_values[i][::-1]
# a=sorted(new_values)

# s=" ".join([i[1:][::-1] for i in a])

# ====>iam ashin from kannur


# Q2 => change the first letter of each word to uppercase
# value = "usman am here go"

# words=value.split()
# uppercase =  " ".join([word.title() for word in words])
# print(uppercase)

# ==>Usman Am Here Go



# Q3 => sort the array in the order of length of the words
values = ['absd','df','sad','k']

for i in range(len(values)-1):
    if len(values[i])< len(values[i+1]):
        values[i],values[i+1]=values[i+1],values[i]

print(values)
