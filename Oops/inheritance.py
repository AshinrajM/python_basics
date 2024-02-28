class Ceo:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("ceo is here")

    def check(self):
        print("salary is 10000")


class Manager(Ceo):

    # def __init__(self,name):
    #     self.name=name

    def display(self):
        print("hey manager here ")

    def check(self):
        print("salary is 5000")


class Staff(Ceo):
    def __init__(self, id, name):
        super().__init__(name)  # here name is passed through super class init method
        self.id = id

    def print_all(self):
        print(f"Name:{self.name}\nID:{self.id}")


m1 = Manager("manager here")
m1.display()
m1.show()
m1.check()

c1 = Ceo("ceo here")
c1.check()

s1 = Staff(2,"akku")
s1.print_all()


# hey manager here
# ceo is here  ==> here manager class is a child class of ceo so it can access all methods which are defined in 
# ceo class salary is 5000 ==> here when we have same method in different classes child class instance will first check is there any method is availeble in its own class if yes it works there if no it will work on the parent class method
# salary is 10000
# Name:akku
# ID:2