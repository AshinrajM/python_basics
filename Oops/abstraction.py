# Abstract class is a class with abstract method . Like in method overriding,
# absract methods are not directly supported by python
# note: If an abstract method is in parent class , child classes must have to 
#       define it.

from abc import ABC,abstractmethod

class Vehicle(ABC):
    def swith_on(self):
        print("switch On")
    def swith_off(self):
        print("swithc Off")

    @abstractmethod
    def change_gear(self):
        pass

class Car(Vehicle):
    def roof_on(self):
        print("sun roof on")
    
    def change_gear(self):
        print("automatic")


class Truck(Vehicle):
    def load_weight(self):
        print("loading weight")
    def change_gear(self):
        print("Manual")

c=Car()
t=Truck()
c.change_gear()
t.change_gear()


# just imagine if we have manual gears for truck and automatic for car . 
# To achieve that we have to declare an abstract method Also want to inherit
# the parent class from ABC because  the abstract method declared class has to
# be abstract class(ABC is abstract class)

