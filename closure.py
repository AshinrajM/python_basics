def wrapper(text):
    msg = text

    def inner():
        print(text)

    return inner


a = wrapper("hieyy")
a()
print(a)
a1 = wrapper("helloooooo")
a1()
print(a1)
a()


# closure (a fucntion ) which will have its own environment and there is
# atleast one bound variable, the environment will keep the bound variable in memory between users of closure. Here the
# a,a1 are the users and "msg"(the argument "text") is the bound variable , thats we can see that a and a1 have different
# memory spaces. here this is the main property of closure,  ie after calling a1 and again calling a the value at msg
# is not overwriting the values of msg.

# output==>
# hieyy
# <function wrapper.<locals>.inner at 0x00000216CC4D8F40>
# helloooooo
# <function wrapper.<locals>.inner at 0x00000216CC4D9E40>
# hieyy
