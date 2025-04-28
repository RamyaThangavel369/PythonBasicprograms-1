#module-a file containing code you want to include in your program
       use 'import' to include a module(built in your own)
       useful to break up a large program resusable separate files.Module same as a code library.
import math
#import math as m
#from math import e
#print(m.pi)
a,b,c,d,e=1,2,3,4,5

print(e**a)
print(e**b)
print(e**c)
print(e**d)
print(e**e)

print(math.e**a)
print(math.e**b)
print(math.e**c)
print(math.e**d)
print(math.e**e)
import moduleexample

result1=moduleexample.pi
result2=moduleexample.square(3)
result3=moduleexample.cube(2)
result4=moduleexample.circumference(2)
result5=moduleexample.area(4)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)


