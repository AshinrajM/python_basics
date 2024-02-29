class Users:
    blood_group = "B+"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Hey!", self.name, "&age!", self.age, self.blood_group)

    @classmethod
    def change(cls, blood_group):
        cls.blood_group = cls.blood_group + blood_group


user1 = Users("salman", 45)
user2 = Users("shukkur", 56)
# Users.blood_group = "O+"  # here the class attribute is changed for all the objects
# user1.blood_group = "A+"  # attribute changed for only user1 object
Users.change("k+")        # here we have callled the class method change
user1.display()
user2.display()



# here i have declared class "Users"  and user1,user2 are the objects of the class and "display" is the
# method we defined in this class
# __init__ is special type of function(magic method) which is automatically called when an object is created


# ==> Hey! salman &age! 45 A+
# ==> Hey! shukkur &age! 56 O+K+
