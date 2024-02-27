class Users:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Hey!", self.name, "&age!", self.age)


user1 = Users("salman", 45)
user2 = Users("shukkur", 56)

user1.display()
user2.display()


# here i have declared class "Users"  and user1,user2 are the objects of the class and "display" is the
# method we defined in this class
#__init__ is special type of function which is automatically called when an object is created
 

# ==> Hey! salman &age! 45
# ==> Hey! shukkur &age! 56
