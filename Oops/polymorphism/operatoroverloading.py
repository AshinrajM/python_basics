class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __add__(self,p):
        p1=self.price
        p2=p.price
        print("total price is",p1+p2)

a=Product("G",1234)
b=Product("K",4565)

a+b

# here we overloaded the inbuilt __add__ method (add is a magic method)
# ie, when the operator is called (a+b) its inbuilt magic method is called the 
# change we made there will work
# o/p ==>total price is 5799