def wrapper(text):
    def inner():
        print(text)
    return inner

a=wrapper("hieyy")
a()