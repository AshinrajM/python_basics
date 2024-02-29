class Bank:
    def __init__(self, balance=100):
        self.__balance = balance

    def get_balance(self):
        print(self.__balance)

    def set_balance(self, amount):
        self.__balance = amount


a = Bank()
a.get_balance()
a.set_balance(1345)
a.get_balance()


# __balance is a marked as private attribute by prefixing double underscore.
# This makes it inaccessible from outside of the class.get_balance and 
# set_balance used to access and modify the balances(getter and setter in other
# languages). 

# output ==> 
# 100
# 1345