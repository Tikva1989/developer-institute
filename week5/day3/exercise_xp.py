#====================Exercise 1 : Built-In Functions=================
# class Program():
#     def __init(self,value):
#         self.value = value
#
#     def __abs__(self):
#         return
#
#     def __int__(self):
#         return  "function converts the specified value into an integer number"
#
#     def __input__(self):

#========================Exercise 2: Currencies=====================

#Create the code which will output the results below.

import rais


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount =  amount

    def __str__(self):
        if self.amount > 1:
             return f'{self.amount} {self.currency}s'
        else:
            return f'{self.amount} {self.currency}'

    def __int__(self):
        return self.amount

    def __repr__(self):
        if self.amount > 1:
            return f'{self.amount} {self.currency}s'
        else:
            return f'{self.amount} {self.currency}'

    def  __add__(self, other):
        if isinstance(other, int):
            return self.amount + int(other)


    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise Exception('Cannot add between Currency type <dollar> and <shekel>')
        self.amount = int(self) + int(other)
        return f"{self.amount} {self.currency}s"


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

# print(str(c1))
# print(int(c1))
# print(repr(c1))
# print(c1 + 5)
# print(c1 + c2)
# print(c1)
# c1 += 5
# print(c1)
# c1 += c2
# print(c1)
# print(c1 + c3)

