class A:
    def latest(self):
        print("latest in A class")

class B(A):
    def latest(self):
        print("latest in B class")
        super().latest()



m = B()
m.latest()


# Here the latest() in A is overriding latest() in B. 
# When we apply the super() , at first the method in that class will work also
# method in parent class also work
