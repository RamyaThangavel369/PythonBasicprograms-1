#1)Iterator:is an object,it returns one item at a time when you call next on it:
#2)__iter__() $ __next__()
#3)StopIteration-stops
"""
my_list=[1,2,3,4,5]
iterator=iter(my_list)#Get the iterator from the iterable
print(next(iterator))#output 1
print(next(iterator))#output 2
print(next(iterator))#output 3
print(next(iterator))#output 5
print(next(iterator))#StoptIteration"""

class MyCounter:
    def __init__(self,limit):

    def __iter__(self):


    def __next__(self):



