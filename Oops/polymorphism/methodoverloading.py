#As because of dynamic typing python doesnt support method overloading 
#but it can be achieved by using 'default arguments'
class Overloading:
    def abc(self,a,b=0):
        print('abc()',a+b)

k=Overloading()
k.abc(12)
k.abc(12,14)

# Like given her we can profide a default arguments which will make method 
# overloading work
# o/p ==>
# abc() 12
# abc() 26